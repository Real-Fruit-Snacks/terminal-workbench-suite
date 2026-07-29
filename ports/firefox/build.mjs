// Generates the Terminal Workbench Firefox theme manifests from tokens.json.
// Usage: node build.mjs
// Token system and design rules per THEME-SPEC.md; thresholds are WCAG AA.
// Companion to ports/brave/build.mjs — the chrome roles the two browsers
// share resolve to the same tokens, so the ports stay in step.
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

const VERSION = '1.2.0';

// Per-variant manifest identity. The dark theme ships as the unqualified
// name because that is what it was published under.
const VARIANTS = {
  dark: { name: 'Terminal Workbench', id: 'terminal-workbench-dark@real-fruit-snacks' },
  light: { name: 'Terminal Workbench Light', id: 'terminal-workbench-light@real-fruit-snacks' },
};

// Menu/sidebar highlight is the spec's selection tint: accent over the popup
// surface, weaker in light mode (THEME-SPEC 2.4, matching --twb-selection).
const SELECTION_MIX = { dark: 0.2, light: 0.17 };
const selectionTint = { mix: 'accent', over: 'bg-1' };

// Firefox theme.colors key -> design token; one mapping for both modes.
//
// Surfaces follow the graphite ramp, stepping away from the page: the tab
// strip sits at the page surface, the toolbar and the selected tab are the
// "title/tab bar" step, and the address field is a form field one step
// further in. Text follows "quiet chrome, loud signal" — near-monochrome
// graphite, accent spent only on the selected tab, its top line, and the
// bookmark bar.
const MAPPING = {
  frame: 'bg-0',                          // tab strip, behind unselected tabs
  frame_inactive: 'bg-0',                 // unfocused window
  toolbar: 'bg-1',
  tab_selected: 'bg-1',                   // seated flush in its bar (spec 5)
  tab_background_text: 'text-muted',      // unselected tab label (spec 5)
  tab_text: 'accent',                     // selected tab label (spec 5)
  tab_line: 'accent',                     // top accent line (spec 5)
  toolbar_text: 'accent',                 // alias of bookmark_text in Firefox
  toolbar_field: 'bg-2',                  // form field (spec 2.2)
  toolbar_field_text: 'text-normal',      // body text, not signal
  toolbar_field_border: 'border',
  toolbar_field_focus: 'bg-3',
  toolbar_top_separator: 'border',
  toolbar_bottom_separator: 'border',
  bookmark_text: 'accent',
  icons: 'text-muted',                    // icons need 3:1, and text-faint
                                          // misses it on light surfaces
  icons_attention: 'accent',
  button_background_hover: 'bg-3',        // hover surface (spec 2.2)
  button_background_active: 'bg-4',
  popup: 'bg-1',
  popup_text: 'text-normal',
  popup_border: 'border',
  popup_highlight: selectionTint,
  popup_highlight_text: 'text-normal',
  sidebar: 'bg-1',
  sidebar_text: 'text-normal',
  sidebar_border: 'border',
  sidebar_highlight: selectionTint,
  sidebar_highlight_text: 'text-normal',
  ntp_background: 'bg-0',                 // page background (spec 2.2)
  ntp_text: 'text-normal',
};

// [foreground key, background key, minimum WCAG ratio]
const CONTRAST_GATE = [
  ['tab_text', 'tab_selected', 4.5],
  ['toolbar_text', 'toolbar', 4.5],
  ['bookmark_text', 'toolbar', 4.5],
  ['toolbar_field_text', 'toolbar_field', 4.5],
  ['toolbar_field_text', 'toolbar_field_focus', 4.5],
  ['popup_text', 'popup', 4.5],
  ['popup_highlight_text', 'popup_highlight', 4.5],
  ['sidebar_text', 'sidebar', 4.5],
  ['sidebar_highlight_text', 'sidebar_highlight', 4.5],
  ['ntp_text', 'ntp_background', 4.5],
  ['tab_background_text', 'frame', 3],
  ['icons', 'toolbar', 3],
  ['icons_attention', 'toolbar', 3],
  ['tab_line', 'tab_selected', 3],
];

export function hexToRgb(hex) {
  const m = /^#([0-9a-f]{6})$/i.exec(hex);
  if (!m) throw new Error(`Bad hex color: ${hex}`);
  return [0, 2, 4].map(i => parseInt(m[1].slice(i, i + 2), 16));
}

function toHex(rgb) {
  return `#${rgb.map(v => v.toString(16).padStart(2, '0')).join('')}`;
}

export function mix(fg, bg, ratio) {
  const [a, b] = [hexToRgb(fg), hexToRgb(bg)];
  return toHex(a.map((v, i) => Math.round(v * ratio + b[i] * (1 - ratio))));
}

function luminance(hex) {
  const [r, g, b] = hexToRgb(hex)
    .map(v => v / 255)
    .map(c => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

export function contrast(hexA, hexB) {
  const [hi, lo] = [luminance(hexA), luminance(hexB)].sort((a, b) => b - a);
  return (hi + 0.05) / (lo + 0.05);
}

export function resolve(mode, tokens) {
  const colors = {};
  for (const [key, token] of Object.entries(MAPPING)) {
    if (typeof token === 'object') {
      colors[key] = mix(tokens[token.mix], tokens[token.over], SELECTION_MIX[mode]);
      continue;
    }
    if (!(token in tokens)) throw new Error(`${mode}: missing token "${token}"`);
    colors[key] = tokens[token];
  }
  return colors;
}

export function buildManifest(mode, tokens) {
  const { name, id } = VARIANTS[mode];
  return {
    manifest_version: 2,
    name,
    description: `Calm graphite terminal-workbench chrome for Firefox — ${mode} mode.`,
    author: 'Real-Fruit-Snacks',
    version: VERSION,
    applications: { gecko: { id } },
    theme: { colors: resolve(mode, tokens) },
  };
}

export function checkContrast(mode, tokens) {
  const colors = resolve(mode, tokens);
  const failures = [];
  for (const [fgKey, bgKey, min] of CONTRAST_GATE) {
    const ratio = contrast(colors[fgKey], colors[bgKey]);
    const ok = ratio >= min;
    console.log(`${ok ? 'PASS' : 'FAIL'} ${ratio.toFixed(2).padStart(5)}:1 (>= ${min}:1) ${mode}: ${fgKey} on ${bgKey}`);
    if (!ok) failures.push(`${mode}: ${fgKey} on ${bgKey} = ${ratio.toFixed(2)}:1 (needs ${min}:1)`);
  }
  return failures;
}

function main() {
  const tokens = JSON.parse(readFileSync(new URL('./tokens.json', import.meta.url), 'utf8'));
  const modes = ['dark', 'light'];

  const failures = modes.flatMap(mode => checkContrast(mode, tokens[mode]));
  if (failures.length) {
    console.error(`\nContrast gate failed — nothing written:\n${failures.join('\n')}`);
    process.exit(1);
  }

  for (const mode of modes) {
    const dir = new URL(`./terminal-workbench-${mode}/`, import.meta.url);
    mkdirSync(dir, { recursive: true });
    writeFileSync(new URL('manifest.json', dir), JSON.stringify(buildManifest(mode, tokens[mode]), null, 2) + '\n');
    console.log(`wrote terminal-workbench-${mode}/manifest.json`);
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) main();
