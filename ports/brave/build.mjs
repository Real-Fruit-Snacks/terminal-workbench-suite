// Generates the Terminal Workbench Brave theme manifests from tokens.json.
// Usage: node build.mjs
// Token system and design rules per THEME-SPEC.md; thresholds are WCAG AA.
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

// Chromium theme.colors key -> design token; one mapping for both modes.
//
// Surfaces follow the THEME-SPEC graphite ramp, stepping away from the page:
// the tab strip sits at the page surface, the toolbar (which Chromium also
// paints behind the active tab) is the "title/tab bar" step, and the omnibox
// is a form field one step further in. Text follows "quiet chrome, loud
// signal" — near-monochrome graphite everywhere, accent spent only on the
// active tab and the bookmark bar, cyan reserved for links.
const MAPPING = {
  frame: 'bg-0',                             // tab strip, behind inactive tabs
  frame_inactive: 'bg-0',                    // unfocused window
  toolbar: 'bg-1',                           // toolbar + active tab block
  tab_text: 'accent',                        // active tab label (spec 5)
  tab_background_text: 'text-muted',         // inactive tab label (spec 5)
  tab_background_text_inactive: 'text-faint', // inactive tab, unfocused window
  omnibox_background: 'bg-2',                // form field (spec 2.2)
  omnibox_text: 'text-normal',               // body text, not signal
  bookmark_text: 'accent',
  toolbar_button_icon: 'text-muted',         // icons need 3:1, and text-faint
                                             // misses it on light surfaces
  ntp_background: 'bg-0',                    // page background (spec 2.2)
  ntp_text: 'text-normal',
  ntp_link: 'accent-alt',                    // links are cyan (spec 2.1)
};

// [foreground key, background key, minimum WCAG ratio]
const CONTRAST_GATE = [
  ['tab_text', 'toolbar', 4.5],
  ['omnibox_text', 'omnibox_background', 4.5],
  ['bookmark_text', 'toolbar', 4.5],
  ['ntp_text', 'ntp_background', 4.5],
  ['ntp_link', 'ntp_background', 4.5],
  ['tab_background_text', 'frame', 3],
  ['tab_background_text_inactive', 'frame', 3],
  ['toolbar_button_icon', 'toolbar', 3],
];

export function hexToRgb(hex) {
  const m = /^#([0-9a-f]{6})$/i.exec(hex);
  if (!m) throw new Error(`Bad hex color: ${hex}`);
  return [0, 2, 4].map(i => parseInt(m[1].slice(i, i + 2), 16));
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

export function buildManifest(mode, tokens) {
  const colors = {};
  for (const [key, token] of Object.entries(MAPPING)) {
    if (!(token in tokens)) throw new Error(`${mode}: missing token "${token}"`);
    colors[key] = hexToRgb(tokens[token]);
  }
  const label = mode[0].toUpperCase() + mode.slice(1);
  return {
    manifest_version: 3,
    name: `Terminal Workbench ${label}`,
    version: '1.8.0',
    description: `Calm graphite terminal-workbench chrome — ${mode} mode.`,
    theme: { colors },
  };
}

export function checkContrast(mode, tokens) {
  const failures = [];
  for (const [fgKey, bgKey, min] of CONTRAST_GATE) {
    const ratio = contrast(tokens[MAPPING[fgKey]], tokens[MAPPING[bgKey]]);
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
    const dir = new URL(`./dist/terminal-workbench-${mode}/`, import.meta.url);
    mkdirSync(dir, { recursive: true });
    writeFileSync(new URL('manifest.json', dir), JSON.stringify(buildManifest(mode, tokens[mode]), null, 2) + '\n');
    console.log(`wrote dist/terminal-workbench-${mode}/manifest.json`);
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) main();
