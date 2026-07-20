'use strict';

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { dark, light } = require('../build/tokens');

const HEX = /^#[0-9a-f]{6}$/;

test('dark and light define the same token set', () => {
  assert.deepEqual(Object.keys(dark).sort(), Object.keys(light).sort());
});

test('all color tokens are lowercase 6-digit hex', () => {
  for (const mode of [dark, light]) {
    for (const [key, value] of Object.entries(mode)) {
      if (key === 'name' || key === 'type') continue;
      assert.match(value, HEX, `${mode.type}.${key} = ${value}`);
    }
  }
});

test('spec anchor values', () => {
  assert.equal(dark.accent, '#63f2ab');
  assert.equal(dark.bg0, '#090c0d');
  assert.equal(dark.codeComment, '#6f807b');
  assert.equal(light.accent, '#007a4d');
  assert.equal(light.bg0, '#f5f7f4');
  assert.equal(light.codeComment, '#5f6f67'); // AA adaptation — see design doc
});

test('mode metadata', () => {
  assert.equal(dark.type, 'dark');
  assert.equal(light.type, 'light');
  assert.equal(dark.name, 'Terminal Workbench');
  assert.equal(light.name, 'Terminal Workbench Light');
});
