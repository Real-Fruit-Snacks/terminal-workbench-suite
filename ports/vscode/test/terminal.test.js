'use strict';

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { terminalColors } = require('../build/terminal');
const { dark, light } = require('../build/tokens');
const { mix } = require('../build/lib/color');

test('ANSI hues map to spec tokens', () => {
  const c = terminalColors(dark, true);
  assert.equal(c['terminal.background'], dark.bg0);
  assert.equal(c['terminal.ansiRed'], dark.red);
  assert.equal(c['terminal.ansiGreen'], dark.accent);
  assert.equal(c['terminal.ansiYellow'], dark.warm);
  assert.equal(c['terminal.ansiBlue'], dark.ansiBlue);
  assert.equal(c['terminal.ansiMagenta'], dark.violet);
  assert.equal(c['terminal.ansiCyan'], dark.accentAlt);
});

test('bright variants mix 12% toward white (dark) / black (light)', () => {
  assert.equal(terminalColors(dark, true)['terminal.ansiBrightGreen'], mix(dark.accent, '#ffffff', 0.12));
  assert.equal(terminalColors(light, false)['terminal.ansiBrightGreen'], mix(light.accent, '#000000', 0.12));
});

test('dark-mode black/white anchors', () => {
  const c = terminalColors(dark, true);
  assert.equal(c['terminal.ansiBlack'], dark.bg4);
  assert.equal(c['terminal.ansiBrightBlack'], dark.textFaint);
  assert.equal(c['terminal.ansiWhite'], dark.textSoft);
  assert.equal(c['terminal.ansiBrightWhite'], dark.textNormal);
});

test('light-mode black/white are legible inks, not surfaces', () => {
  const c = terminalColors(light, false);
  assert.equal(c['terminal.ansiBlack'], light.textNormal);
  assert.equal(c['terminal.ansiBrightBlack'], light.textSoft);
  assert.equal(c['terminal.ansiWhite'], light.textMuted);
  assert.equal(c['terminal.ansiBrightWhite'], light.textFaint);
});
