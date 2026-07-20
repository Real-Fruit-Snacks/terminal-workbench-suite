'use strict';

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { extensionChips, fileNameChips, chipDefs, iconSvgs, iconManifest, chipTextAttrs } = require('../build/icons');
const { dark, light } = require('../build/tokens');
const { alpha } = require('../build/lib/color');
const fs = require('node:fs');
const path = require('node:path');

test('chip table is well-formed', () => {
  for (const e of [...extensionChips, ...fileNameChips]) {
    assert.match(e.chip, /^[A-Z0-9]{1,4}$/, `bad chip ${e.chip}`);
    assert.ok(e.hue in dark && e.hue in light, `unknown hue token ${e.hue}`);
  }
  assert.ok(chipDefs().size > 30, 'expected broad type coverage');
});

test('sizing rule follows the spec', () => {
  assert.deepEqual(chipTextAttrs('TS'), { size: 7, textLength: null });
  assert.deepEqual(chipTextAttrs('CSS'), { size: 6, textLength: 12.5 });
  assert.deepEqual(chipTextAttrs('HTML'), { size: 5.2, textLength: 13.5 });
});

test('chip svgs use the tag recipe from the hue token', () => {
  const svgs = iconSvgs(dark);
  const ts = svgs['chip-ts'];
  assert.ok(ts.includes(`fill="${alpha(dark.accentAlt, 0.13)}"`), 'chip fill = hue @13%');
  assert.ok(ts.includes(`stroke="${alpha(dark.accentAlt, 0.28)}"`), 'chip stroke = hue @28%');
  assert.ok(ts.includes(`fill="${dark.accentAlt}"`), 'chip text = hue');
  assert.ok(ts.includes('>TS<'));
});

test('every svg is structurally sound with lowercase hex only', () => {
  for (const t of [dark, light]) {
    for (const [name, svg] of Object.entries(iconSvgs(t))) {
      assert.ok(svg.startsWith('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">'), name);
      assert.ok(svg.trimEnd().endsWith('</svg>'), name);
      for (const hex of svg.match(/#[0-9a-fA-F]+/g) ?? []) {
        assert.match(hex, /^#[0-9a-f]{6}([0-9a-f]{2})?$/, `${name}: ${hex}`);
      }
    }
  }
});

test('folders and generic file are quiet; open folder carries accent', () => {
  const svgs = iconSvgs(dark);
  assert.ok(svgs.folder.includes(`stroke="${dark.textFaint}"`));
  assert.ok(svgs.file.includes(`stroke="${dark.textFaint}"`));
  assert.ok(svgs['folder-open'].includes(`stroke="${dark.accent}"`));
});

test('manifest maps every table entry and lights every mapping', () => {
  const m = iconManifest();
  for (const e of extensionChips) {
    for (const ext of e.extensions) {
      assert.equal(m.fileExtensions[ext], `_chip-${e.chip.toLowerCase()}`);
      assert.equal(m.light.fileExtensions[ext], `_chip-${e.chip.toLowerCase()}_light`);
    }
  }
  for (const e of fileNameChips) {
    for (const fn of e.fileNames) {
      assert.equal(m.fileNames[fn], `_chip-${e.chip.toLowerCase()}`);
      assert.equal(m.light.fileNames[fn], `_chip-${e.chip.toLowerCase()}_light`);
    }
  }
  const allIds = [
    ...Object.values(m.fileExtensions), ...Object.values(m.fileNames),
    ...Object.values(m.light.fileExtensions), ...Object.values(m.light.fileNames),
    m.file, m.folder, m.folderExpanded, m.light.file, m.light.folder, m.light.folderExpanded,
  ];
  for (const id of allIds) assert.ok(m.iconDefinitions[id], `undefined icon id ${id}`);
  assert.equal(m.folder, '_folder');
  assert.equal(m.folderExpanded, '_folder-open');
  assert.equal(m.file, '_file');
  assert.equal(m.hidesExplorerArrows, false);
});

test('generated icons and manifest are in sync with the builder', () => {
  const iconDir = path.join(__dirname, '..', 'icons');
  for (const t of [dark, light]) {
    const suffix = t.type === 'dark' ? '' : '-light';
    for (const [name, svg] of Object.entries(iconSvgs(t))) {
      const p = path.join(iconDir, `${name}${suffix}.svg`);
      assert.ok(fs.existsSync(p), `${name}${suffix}.svg missing — run: node build/build.js`);
      assert.equal(fs.readFileSync(p, 'utf8'), svg);
    }
  }
  const onDisk = fs.readdirSync(iconDir).filter((f) => f.endsWith('.svg'));
  assert.equal(onDisk.length, Object.keys(iconSvgs(dark)).length * 2, 'stale files in icons/');
  const manifestPath = path.join(__dirname, '..', 'themes', 'terminal-workbench-file-icons.json');
  assert.deepEqual(JSON.parse(fs.readFileSync(manifestPath, 'utf8')), JSON.parse(JSON.stringify(iconManifest())));
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const themesDir = path.dirname(manifestPath);
  for (const def of Object.values(manifest.iconDefinitions)) {
    assert.ok(fs.existsSync(path.resolve(themesDir, def.iconPath)), `unresolvable iconPath ${def.iconPath}`);
  }
});

test('package.json contributes the icon theme at an existing path', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'package.json'), 'utf8'));
  const it = pkg.contributes.iconThemes;
  assert.equal(it.length, 1);
  assert.equal(it[0].id, 'terminal-workbench-icons');
  assert.equal(it[0].label, 'Terminal Workbench Icons');
  assert.ok(fs.existsSync(path.join(__dirname, '..', it[0].path)));
  assert.equal(pkg.version, '0.2.0');
});
