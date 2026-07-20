'use strict';

const { test } = require('node:test');
const assert = require('node:assert/strict');
const { tokenColors, semanticTokenColors } = require('../build/syntax');
const { dark } = require('../build/tokens');

function ruleFor(rules, scope) {
  return rules.find((r) => (Array.isArray(r.scope) ? r.scope.includes(scope) : r.scope === scope));
}

test('no fontStyle anywhere — flat weight', () => {
  const rules = tokenColors(dark);
  for (const r of rules) {
    assert.ok(!('fontStyle' in r.settings), `rule "${r.name}" sets fontStyle`);
    assert.ok(!/italic|bold|fontstyle/i.test(r.name), `rule name "${r.name}" mentions styling`);
  }
  for (const [token, value] of Object.entries(semanticTokenColors(dark))) {
    assert.equal(typeof value, 'string', `semantic ${token} must be a plain color string`);
    assert.match(value, /^#[0-9a-f]{6}$/, `semantic ${token} = ${value}`);
  }
});

test('core scheme follows theme.css / spec', () => {
  const rules = tokenColors(dark);
  assert.equal(ruleFor(rules, 'comment').settings.foreground, dark.codeComment);
  assert.equal(ruleFor(rules, 'string').settings.foreground, dark.accent);
  assert.equal(ruleFor(rules, 'keyword').settings.foreground, dark.violet);
  assert.equal(ruleFor(rules, 'entity.name.function').settings.foreground, dark.accentAlt);
  assert.equal(ruleFor(rules, 'constant.numeric').settings.foreground, dark.orange);
  assert.equal(ruleFor(rules, 'entity.other.attribute-name').settings.foreground, dark.warm);
  assert.equal(ruleFor(rules, 'entity.name.tag').settings.foreground, dark.red);
  assert.equal(ruleFor(rules, 'punctuation').settings.foreground, dark.textMuted);
});

test('adaptations: quiet operators, cyan types, YAML keys not red', () => {
  const rules = tokenColors(dark);
  assert.equal(ruleFor(rules, 'keyword.operator').settings.foreground, dark.textSoft);
  assert.equal(ruleFor(rules, 'entity.name.type').settings.foreground, dark.accentAlt);
  assert.equal(ruleFor(rules, 'entity.name.tag.yaml').settings.foreground, dark.warm);
});

test('markdown headings follow the prose scale', () => {
  const rules = tokenColors(dark);
  assert.equal(ruleFor(rules, 'heading.1.markdown').settings.foreground, dark.textNormal);
  assert.equal(ruleFor(rules, 'heading.2.markdown').settings.foreground, dark.accent);
  assert.equal(ruleFor(rules, 'heading.3.markdown').settings.foreground, dark.accentAlt);
  assert.equal(ruleFor(rules, 'heading.4.markdown').settings.foreground, dark.warm);
});

test('semantic tokens mirror the TextMate scheme', () => {
  const s = semanticTokenColors(dark);
  assert.equal(s.string, dark.accent);
  assert.equal(s.keyword, dark.violet);
  assert.equal(s.function, dark.accentAlt);
  assert.equal(s.type, dark.accentAlt);
  assert.equal(s.property, dark.warm);
  assert.equal(s.comment, dark.codeComment);
  assert.equal(s.operator, dark.textSoft);
});
