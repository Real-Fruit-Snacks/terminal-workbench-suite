'use strict';

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { workbenchColors } = require('../build/workbench');
const { dark, light } = require('../build/tokens');
const { alpha } = require('../build/lib/color');

const HEX = /^#[0-9a-f]{6}([0-9a-f]{2})?$/;

test('every value is valid 6- or 8-digit lowercase hex', () => {
  for (const t of [dark, light]) {
    const colors = workbenchColors(t, t.type === 'dark');
    assert.ok(Object.keys(colors).length > 150, 'expected a substantial key set');
    for (const [key, value] of Object.entries(colors)) {
      assert.match(value, HEX, `${t.type} ${key} = ${value}`);
    }
  }
});

test('layering: editor bg0, chrome bg1, widgets bg2, raised bg3/bg4', () => {
  const c = workbenchColors(dark, true);
  assert.equal(c['editor.background'], dark.bg0);
  assert.equal(c['sideBar.background'], dark.bg1);
  assert.equal(c['statusBar.background'], dark.bg1);
  assert.equal(c['input.background'], dark.bg2);
  assert.equal(c['editorWidget.background'], dark.bg2);
  assert.equal(c['tab.activeBackground'], dark.bg3);
  assert.equal(c['menu.background'], dark.bg4);
});

test('signal: accent only where it means something', () => {
  const c = workbenchColors(dark, true);
  assert.equal(c['tab.activeForeground'], dark.accent);
  assert.equal(c['button.background'], dark.accent);
  assert.equal(c['badge.background'], dark.accent);
  assert.equal(c['textLink.foreground'], dark.accentAlt);
  assert.equal(c['activityBar.activeBorder'], dark.accent);
});

test('derived tints follow the spec §2.4 recipes', () => {
  const cd = workbenchColors(dark, true);
  const cl = workbenchColors(light, false);
  assert.equal(cd['editor.selectionBackground'], alpha(dark.accent, 0.2));
  assert.equal(cl['editor.selectionBackground'], alpha(light.accent, 0.17));
  assert.equal(cd['editor.lineHighlightBackground'], alpha(dark.accentAlt, 0.075));
  assert.equal(cd.focusBorder, alpha(dark.accent, 0.18));
  assert.equal(cd['editor.findMatchBackground'], alpha(dark.warm, 0.22));
  assert.equal(cd['list.activeSelectionBackground'], alpha(dark.accent, 0.105));
});

test('status bar stays graphite in both modes', () => {
  for (const t of [dark, light]) {
    const c = workbenchColors(t, t.type === 'dark');
    assert.equal(c['statusBar.background'], t.bg1);
    assert.equal(c['statusBar.foreground'], t.textMuted);
  }
});

test('list selection keeps syntax/git colors — foreground stays unset', () => {
  for (const t of [dark, light]) {
    const c = workbenchColors(t, t.type === 'dark');
    assert.ok(!('list.activeSelectionForeground' in c), 'list.activeSelectionForeground must be unset');
  }
});
