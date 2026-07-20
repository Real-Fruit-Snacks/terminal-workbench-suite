'use strict';

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { alpha, mix, lighten, darken, contrast } = require('../build/lib/color');

test('alpha appends a 2-digit hex alpha and lowercases', () => {
  assert.equal(alpha('#63f2ab', 0.2), '#63f2ab33');
  assert.equal(alpha('#FFFFFF', 1), '#ffffffff');
  assert.equal(alpha('#000000', 0), '#00000000');
  assert.equal(alpha('#6bdcff', 0.075), '#6bdcff13');
  assert.equal(alpha('#63f2ab', 0.18), '#63f2ab2e');
});

test('mix blends channels linearly toward the second color', () => {
  assert.equal(mix('#000000', '#ffffff', 0.5), '#808080');
  assert.equal(mix('#000000', '#ffffff', 0), '#000000');
  assert.equal(mix('#000000', '#ffffff', 1), '#ffffff');
});

test('lighten and darken are mixes toward white/black', () => {
  assert.equal(lighten('#000000', 1), '#ffffff');
  assert.equal(darken('#ffffff', 1), '#000000');
  assert.equal(lighten('#63f2ab', 0), '#63f2ab');
});

test('contrast matches WCAG reference values and is symmetric', () => {
  assert.equal(contrast('#000000', '#ffffff'), 21);
  assert.equal(contrast('#ffffff', '#ffffff'), 1);
  assert.equal(contrast('#63f2ab', '#090c0d'), contrast('#090c0d', '#63f2ab'));
  assert.ok(contrast('#dce4df', '#090c0d') > 4.5);
});
