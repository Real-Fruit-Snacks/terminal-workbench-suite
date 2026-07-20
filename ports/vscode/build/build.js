'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { dark, light } = require('./tokens');
const { workbenchColors } = require('./workbench');
const { tokenColors, semanticTokenColors } = require('./syntax');
const { terminalColors } = require('./terminal');
const { contrast, luminance } = require('./lib/color');
const { iconSvgs, iconManifest } = require('./icons');
const { coverSvg } = require('./cover');

function buildTheme(t) {
  const isDark = t.type === 'dark';
  return {
    name: t.name,
    type: t.type,
    semanticHighlighting: true,
    colors: { ...workbenchColors(t, isDark), ...terminalColors(t, isDark) },
    tokenColors: tokenColors(t),
    semanticTokenColors: semanticTokenColors(t),
  };
}

// Body-size text is a hard AA gate (spec §2.3). Hue tokens warn only —
// their values are locked by THEME-SPEC, and two light-mode hues sit
// just under 4.5 (warm ≈4.35, orange ≈4.44 on bg0). Expected, accepted.
const BODY_PAIRS = [
  ['textNormal', 'bg0'], ['textNormal', 'bg1'], ['textNormal', 'bg2'],
  ['textSoft', 'bg0'], ['textSoft', 'bg2'],
  ['textMuted', 'bg0'], ['textMuted', 'bg1'],
  ['codeComment', 'bg0'],
  ['textOnAccent', 'accent'],
];
const HUE_PAIRS = [
  ['accent', 'bg0'], ['accentAlt', 'bg0'], ['warm', 'bg0'],
  ['red', 'bg0'], ['orange', 'bg0'], ['violet', 'bg0'], ['ansiBlue', 'bg0'],
];

function checkContrast(t) {
  const row = (fg, bg, kind) => {
    const ratio = contrast(t[fg], t[bg]);
    const level = ratio >= 4.5 ? 'pass' : kind === 'body' ? 'fail' : 'warn';
    return { fg, bg, ratio, level };
  };
  return [
    ...BODY_PAIRS.map(([fg, bg]) => row(fg, bg, 'body')),
    ...HUE_PAIRS.map(([fg, bg]) => row(fg, bg, 'hue')),
  ];
}

// Raw luminance ratio between adjacent surface steps (spec §2.2 target
// ~1.1:1). Informational — the spec's own light ramp sits at 1.04–1.10.
function surfaceGaps(t) {
  const ramp = ['bg0', 'bg1', 'bg2', 'bg3', 'bg4'];
  const rows = [];
  for (let i = 0; i < ramp.length - 1; i++) {
    const la = luminance(t[ramp[i]]);
    const lb = luminance(t[ramp[i + 1]]);
    rows.push({ from: ramp[i], to: ramp[i + 1], ratio: Math.max(la, lb) / Math.min(la, lb) });
  }
  return rows;
}

function main() {
  const outDir = path.join(__dirname, '..', 'themes');
  fs.mkdirSync(outDir, { recursive: true });
  let failed = false;

  for (const t of [dark, light]) {
    const file = `terminal-workbench-${t.type}-color-theme.json`;
    fs.writeFileSync(path.join(outDir, file), JSON.stringify(buildTheme(t), null, 2) + '\n');
    console.log(`\nWrote themes/${file}`);

    console.log(`${t.name} — text contrast (WCAG AA target 4.5:1)`);
    for (const r of checkContrast(t)) {
      const mark = r.level === 'pass' ? 'PASS' : r.level === 'warn' ? 'WARN' : 'FAIL';
      if (r.level === 'fail') failed = true;
      console.log(`  ${mark}  ${r.fg.padEnd(13)} on ${r.bg.padEnd(7)} ${r.ratio.toFixed(2)}:1`);
    }

    console.log(`${t.name} — adjacent surface luminance gaps (spec target ~1.1:1, informational)`);
    for (const g of surfaceGaps(t)) {
      console.log(`  ${g.from} -> ${g.to}  ${g.ratio.toFixed(2)}:1`);
    }
  }

  const iconDir = path.join(__dirname, '..', 'icons');
  fs.mkdirSync(iconDir, { recursive: true });
  for (const [name, svg] of Object.entries(iconSvgs(dark))) {
    fs.writeFileSync(path.join(iconDir, `${name}.svg`), svg);
  }
  for (const [name, svg] of Object.entries(iconSvgs(light))) {
    fs.writeFileSync(path.join(iconDir, `${name}-light.svg`), svg);
  }
  fs.writeFileSync(
    path.join(outDir, 'terminal-workbench-file-icons.json'),
    JSON.stringify(iconManifest(), null, 2) + '\n'
  );
  console.log(`\nWrote ${Object.keys(iconSvgs(dark)).length * 2} icons + themes/terminal-workbench-file-icons.json`);

  const assetDir = path.join(__dirname, '..', 'docs', 'assets');
  fs.mkdirSync(assetDir, { recursive: true });
  fs.writeFileSync(path.join(assetDir, 'cover-dark.svg'), coverSvg(dark));
  fs.writeFileSync(path.join(assetDir, 'cover-light.svg'), coverSvg(light));
  console.log('Wrote docs/assets/cover-dark.svg + cover-light.svg');

  if (failed) {
    console.error('\nBody-text contrast below WCAG AA — fix before shipping.');
    process.exit(1);
  }
  console.log('\nAll body-text contrast checks passed.');
}

module.exports = { buildTheme, checkContrast, surfaceGaps };

if (require.main === module) main();
