'use strict';

const { alpha } = require('./lib/color');

// Type table — the single source of truth for chip icons.
// Extending coverage is adding a row. Hues follow the palette's semantics:
// red = markup tags, warm = config/data (and JS by yellow convention),
// orange = shells/scripts, violet = keyword-heavy languages and styling,
// accentAlt = app languages, accent = Python/Vue, textSoft/textFaint = quiet.
const extensionChips = [
  { chip: 'TS', hue: 'accentAlt', extensions: ['ts'] },
  { chip: 'TSX', hue: 'accentAlt', extensions: ['tsx'] },
  { chip: 'JS', hue: 'warm', extensions: ['js', 'mjs', 'cjs'] },
  { chip: 'JSX', hue: 'warm', extensions: ['jsx'] },
  { chip: 'PY', hue: 'accent', extensions: ['py'] },
  { chip: 'VUE', hue: 'accent', extensions: ['vue'] },
  { chip: 'GO', hue: 'accentAlt', extensions: ['go'] },
  { chip: 'SQL', hue: 'accentAlt', extensions: ['sql'] },
  { chip: 'RS', hue: 'orange', extensions: ['rs'] },
  { chip: 'RB', hue: 'red', extensions: ['rb'] },
  { chip: 'JAVA', hue: 'orange', extensions: ['java'] },
  { chip: 'C', hue: 'violet', extensions: ['c'] },
  { chip: 'H', hue: 'violet', extensions: ['h'] },
  { chip: 'CPP', hue: 'violet', extensions: ['cpp', 'cc'] },
  { chip: 'HPP', hue: 'violet', extensions: ['hpp'] },
  { chip: 'CS', hue: 'violet', extensions: ['cs'] },
  { chip: 'PHP', hue: 'violet', extensions: ['php'] },
  { chip: 'LUA', hue: 'violet', extensions: ['lua'] },
  { chip: 'SH', hue: 'orange', extensions: ['sh', 'bash', 'zsh'] },
  { chip: 'PS1', hue: 'orange', extensions: ['ps1'] },
  { chip: 'BAT', hue: 'orange', extensions: ['bat', 'cmd'] },
  { chip: 'HTML', hue: 'red', extensions: ['html', 'htm'] },
  { chip: 'XML', hue: 'red', extensions: ['xml'] },
  { chip: 'SVG', hue: 'orange', extensions: ['svg'] },
  { chip: 'CSS', hue: 'violet', extensions: ['css'] },
  { chip: 'SCSS', hue: 'violet', extensions: ['scss', 'sass'] },
  { chip: 'LESS', hue: 'violet', extensions: ['less'] },
  { chip: 'JSON', hue: 'warm', extensions: ['json', 'jsonc'] },
  { chip: 'YML', hue: 'warm', extensions: ['yml', 'yaml'] },
  { chip: 'TOML', hue: 'warm', extensions: ['toml'] },
  { chip: 'CFG', hue: 'warm', extensions: ['ini', 'cfg', 'conf'] },
  { chip: 'ENV', hue: 'warm', extensions: ['env'] },
  { chip: 'MD', hue: 'textSoft', extensions: ['md', 'markdown'] },
  { chip: 'TXT', hue: 'textFaint', extensions: ['txt'] },
  { chip: 'LOG', hue: 'textFaint', extensions: ['log'] },
  { chip: 'LOCK', hue: 'textFaint', extensions: ['lock'] },
  { chip: 'IMG', hue: 'textFaint', extensions: ['png', 'jpg', 'jpeg', 'gif', 'webp', 'ico', 'bmp'] },
  { chip: 'PDF', hue: 'red', extensions: ['pdf'] },
  { chip: 'ZIP', hue: 'textFaint', extensions: ['zip', 'tar', 'gz', '7z'] },
  { chip: 'FNT', hue: 'textFaint', extensions: ['ttf', 'otf', 'woff', 'woff2'] },
];

const fileNameChips = [
  { chip: 'DOCK', hue: 'accentAlt', fileNames: ['dockerfile'] },
  { chip: 'MK', hue: 'orange', fileNames: ['makefile'] },
  { chip: 'LIC', hue: 'textFaint', fileNames: ['license', 'license.md', 'license.txt'] },
  { chip: 'GIT', hue: 'textFaint', fileNames: ['.gitignore', '.gitattributes', '.gitmodules'] },
  { chip: 'CFG', hue: 'warm', fileNames: ['.editorconfig'] },
  { chip: 'ENV', hue: 'warm', fileNames: ['.env', '.env.local', '.env.example'] },
];

const FONT = "'Cascadia Code','Consolas','SF Mono','Menlo',monospace";

// Sizing per abbreviation length (spec). textLength pins layout across
// OS font metric differences.
function chipTextAttrs(chip) {
  if (chip.length <= 2) return { size: 7, textLength: null };
  if (chip.length === 3) return { size: 6, textLength: 12.5 };
  return { size: 5.2, textLength: 13.5 };
}

// Deduped icon definitions: CFG/ENV appear in both tables with the same
// hue and share one definition. Same name with different hues is a bug.
function chipDefs() {
  const map = new Map();
  for (const e of [...extensionChips, ...fileNameChips]) {
    const name = `chip-${e.chip.toLowerCase()}`;
    const prev = map.get(name);
    if (prev && prev.hue !== e.hue) throw new Error(`chip ${e.chip} maps to two hues`);
    map.set(name, { chip: e.chip, hue: e.hue });
  }
  return map;
}

// The theme's tag recipe at icon scale: hue @13% fill, @28% stroke.
function chipSvg(hueHex, chip) {
  const { size, textLength } = chipTextAttrs(chip);
  const tl = textLength === null ? '' : ` textLength="${textLength}" lengthAdjust="spacingAndGlyphs"`;
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">' +
    `<rect x="0.5" y="2.5" width="15" height="11" rx="2.5" fill="${alpha(hueHex, 0.13)}" stroke="${alpha(hueHex, 0.28)}"/>` +
    `<text x="8" y="9.9" text-anchor="middle" font-family="${FONT}" font-size="${size}" font-weight="600" fill="${hueHex}"${tl}>${chip}</text>` +
    '</svg>\n';
}

function folderSvg(stroke) {
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">' +
    `<path d="M1.5 4.5 h4.7 l1.6 1.8 h6.7 a0.9 0.9 0 0 1 0.9 0.9 v5 a0.9 0.9 0 0 1 -0.9 0.9 H2.4 a0.9 0.9 0 0 1 -0.9 -0.9 z" fill="none" stroke="${stroke}" stroke-width="1.2" stroke-linejoin="round"/>` +
    '</svg>\n';
}

function folderOpenSvg(stroke) {
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">' +
    `<path d="M1.5 12.2 V4.5 h4.7 l1.6 1.8 h5.4 v1.5" fill="none" stroke="${stroke}" stroke-width="1.2" stroke-linejoin="round"/>` +
    `<path d="M3.2 7.8 h11.3 l-1.9 5.3 H1.5 z" fill="none" stroke="${stroke}" stroke-width="1.2" stroke-linejoin="round"/>` +
    '</svg>\n';
}

function fileSvg(stroke) {
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">' +
    `<path d="M4.2 1.5 h5.3 l3.3 3.3 v9.7 H4.2 z" fill="none" stroke="${stroke}" stroke-width="1.2" stroke-linejoin="round"/>` +
    `<path d="M9.5 1.5 v3.3 h3.3" fill="none" stroke="${stroke}" stroke-width="1.2"/>` +
    '</svg>\n';
}

// All SVGs for one mode, keyed by definition base name.
function iconSvgs(t) {
  const svgs = {
    folder: folderSvg(t.textFaint),
    'folder-open': folderOpenSvg(t.accent),
    file: fileSvg(t.textFaint),
  };
  for (const [name, def] of chipDefs()) {
    svgs[name] = chipSvg(t[def.hue], def.chip);
  }
  return svgs;
}

// Icon theme JSON. iconPath is relative to the manifest file in themes/.
function iconManifest() {
  const iconDefinitions = {};
  const addDef = (name) => {
    iconDefinitions[`_${name}`] = { iconPath: `../icons/${name}.svg` };
    iconDefinitions[`_${name}_light`] = { iconPath: `../icons/${name}-light.svg` };
  };
  addDef('folder');
  addDef('folder-open');
  addDef('file');
  for (const name of chipDefs().keys()) addDef(name);

  const fileExtensions = {};
  for (const e of extensionChips) {
    for (const ext of e.extensions) fileExtensions[ext] = `_chip-${e.chip.toLowerCase()}`;
  }
  const fileNames = {};
  for (const e of fileNameChips) {
    for (const fn of e.fileNames) fileNames[fn] = `_chip-${e.chip.toLowerCase()}`;
  }
  const lightMap = (obj) => Object.fromEntries(Object.entries(obj).map(([k, v]) => [k, `${v}_light`]));

  return {
    iconDefinitions,
    file: '_file',
    folder: '_folder',
    folderExpanded: '_folder-open',
    fileExtensions,
    fileNames,
    light: {
      file: '_file_light',
      folder: '_folder_light',
      folderExpanded: '_folder-open_light',
      fileExtensions: lightMap(fileExtensions),
      fileNames: lightMap(fileNames),
    },
    hidesExplorerArrows: false,
  };
}

module.exports = { extensionChips, fileNameChips, chipDefs, chipTextAttrs, iconSvgs, iconManifest };
