'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { buildTheme, checkContrast } = require('../build/build');
const { dark, light } = require('../build/tokens');

test('buildTheme produces a complete VS Code theme object', () => {
  for (const t of [dark, light]) {
    const theme = buildTheme(t);
    assert.equal(theme.name, t.name);
    assert.equal(theme.type, t.type);
    assert.equal(theme.semanticHighlighting, true);
    assert.equal(theme.colors['editor.background'], t.bg0);
    assert.equal(theme.colors['terminal.ansiGreen'], t.accent);
    assert.ok(Array.isArray(theme.tokenColors) && theme.tokenColors.length > 20);
    assert.ok(theme.semanticTokenColors.function);
  }
});

test('body-text contrast pairs all meet WCAG AA in both modes', () => {
  for (const t of [dark, light]) {
    const failures = checkContrast(t).filter((r) => r.level === 'fail');
    assert.deepEqual(failures, [], `${t.type}: ${JSON.stringify(failures)}`);
  }
});

test('only the two expected light-mode hue warnings exist', () => {
  const darkWarns = checkContrast(dark).filter((r) => r.level === 'warn');
  assert.deepEqual(darkWarns, []);
  const lightWarns = checkContrast(light).filter((r) => r.level === 'warn').map((r) => r.fg).sort();
  assert.deepEqual(lightWarns, ['orange', 'warm']);
});

test('generated theme files exist and are in sync with the builder', () => {
  const cases = [
    [dark, 'terminal-workbench-dark-color-theme.json'],
    [light, 'terminal-workbench-light-color-theme.json'],
  ];
  for (const [t, file] of cases) {
    const p = path.join(__dirname, '..', 'themes', file);
    assert.ok(fs.existsSync(p), `${file} missing — run: node build/build.js`);
    const onDisk = JSON.parse(fs.readFileSync(p, 'utf8'));
    assert.deepEqual(onDisk, JSON.parse(JSON.stringify(buildTheme(t))));
  }
});

test('package.json contributes both themes at the generated paths', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'package.json'), 'utf8'));
  const themes = pkg.contributes.themes;
  assert.equal(themes.length, 2);
  assert.deepEqual(themes.map((x) => x.label), ['Terminal Workbench', 'Terminal Workbench Light']);
  assert.deepEqual(themes.map((x) => x.uiTheme), ['vs-dark', 'vs']);
  for (const th of themes) {
    assert.ok(fs.existsSync(path.join(__dirname, '..', th.path)), `${th.path} missing`);
  }
});
