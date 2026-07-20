'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { coverSvg } = require('../build/cover');
const { dark, light } = require('../build/tokens');

test('cover panel and wordmark come from the tokens', () => {
  for (const t of [dark, light]) {
    const svg = coverSvg(t);
    assert.ok(svg.startsWith('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 460">'));
    assert.ok(svg.includes(`fill="${t.bg0}" stroke="${t.border}"`), 'panel uses bg0 + border');
    assert.ok(svg.includes('>terminal<') && svg.includes('>workbench<'), 'wordmark present');
    assert.ok(svg.includes(`fill="${t.accent}">signal.</tspan>`), 'tagline accent word');
    assert.ok(svg.trimEnd().endsWith('</svg>'));
    for (const hex of svg.match(/#[0-9a-fA-F]+/g) ?? []) {
      assert.match(hex, /^#[0-9a-f]{6}([0-9a-f]{2})?$/, hex);
    }
  }
});

test('generated covers are in sync with the builder', () => {
  const cases = [[dark, 'cover-dark.svg'], [light, 'cover-light.svg']];
  for (const [t, file] of cases) {
    const p = path.join(__dirname, '..', 'docs', 'assets', file);
    assert.ok(fs.existsSync(p), `${file} missing — run: node build/build.js`);
    assert.equal(fs.readFileSync(p, 'utf8'), coverSvg(t));
  }
});
