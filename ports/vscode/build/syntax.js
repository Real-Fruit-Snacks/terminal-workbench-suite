'use strict';

// TextMate token colors. No fontStyle anywhere — flat weight by design.
// Scheme follows THEME-SPEC §2.1 + the Obsidian theme.css token mapping,
// with two documented adaptations: operators are quiet, types share cyan
// with functions.
function tokenColors(t) {
  return [
    { name: 'Comment', scope: ['comment', 'punctuation.definition.comment'], settings: { foreground: t.codeComment } },
    { name: 'String', scope: ['string', 'punctuation.definition.string'], settings: { foreground: t.accent } },
    { name: 'String escape', scope: ['constant.character.escape', 'constant.other.placeholder'], settings: { foreground: t.accentAlt } },
    { name: 'Template expression punctuation', scope: ['punctuation.definition.template-expression', 'punctuation.section.embedded'], settings: { foreground: t.violet } },
    { name: 'Regex', scope: ['string.regexp'], settings: { foreground: t.orange } },
    { name: 'Keyword and storage', scope: ['keyword', 'storage', 'storage.type', 'storage.modifier'], settings: { foreground: t.violet } },
    { name: 'Operator (quiet — adaptation from theme.css mint)', scope: ['keyword.operator'], settings: { foreground: t.textSoft } },
    { name: 'Word-like operators stay keywords', scope: ['keyword.operator.new', 'keyword.operator.expression', 'keyword.operator.wordlike', 'keyword.operator.logical.python'], settings: { foreground: t.violet } },
    { name: 'Function', scope: ['entity.name.function', 'support.function', 'meta.function-call.generic'], settings: { foreground: t.accentAlt } },
    { name: 'Type and class (shares cyan with functions — adaptation)', scope: ['entity.name.type', 'entity.name.class', 'entity.name.namespace', 'entity.other.inherited-class', 'support.type', 'support.class'], settings: { foreground: t.accentAlt } },
    { name: 'Constant and number', scope: ['constant.numeric', 'constant.language', 'constant.other', 'variable.other.enummember', 'keyword.other.unit'], settings: { foreground: t.orange } },
    { name: 'Property and attribute', scope: ['variable.other.property', 'variable.other.object.property', 'support.type.property-name', 'entity.other.attribute-name', 'meta.object-literal.key'], settings: { foreground: t.warm } },
    { name: 'HTML/XML tag', scope: ['entity.name.tag', 'punctuation.definition.tag'], settings: { foreground: t.red } },
    { name: 'YAML key (deeper scope beats entity.name.tag red)', scope: ['entity.name.tag.yaml'], settings: { foreground: t.warm } },
    { name: 'Variable and parameter', scope: ['variable', 'variable.parameter', 'meta.definition.variable'], settings: { foreground: t.textNormal } },
    { name: 'Punctuation', scope: ['punctuation', 'meta.brace'], settings: { foreground: t.textMuted } },
    { name: 'Invalid', scope: ['invalid', 'invalid.illegal', 'invalid.deprecated'], settings: { foreground: t.red } },

    // Markdown — prose scale from THEME-SPEC §3
    { name: 'MD h1', scope: ['heading.1.markdown', 'markup.heading.setext.1.markdown'], settings: { foreground: t.textNormal } },
    { name: 'MD h2', scope: ['heading.2.markdown', 'markup.heading.setext.2.markdown'], settings: { foreground: t.accent } },
    { name: 'MD h3', scope: ['heading.3.markdown'], settings: { foreground: t.accentAlt } },
    { name: 'MD h4', scope: ['heading.4.markdown'], settings: { foreground: t.warm } },
    { name: 'MD h5/h6', scope: ['heading.5.markdown', 'heading.6.markdown'], settings: { foreground: t.textMuted } },
    { name: 'MD emphasis markers (color only)', scope: ['markup.bold', 'markup.italic'], settings: { foreground: t.textNormal } },
    { name: 'MD code', scope: ['markup.inline.raw', 'markup.fenced_code.block'], settings: { foreground: t.textSoft } },
    { name: 'MD quote', scope: ['markup.quote'], settings: { foreground: t.textMuted } },
    { name: 'MD link text', scope: ['string.other.link', 'constant.other.reference.link'], settings: { foreground: t.accentAlt } },
    { name: 'MD link url', scope: ['markup.underline.link'], settings: { foreground: t.textMuted } },
    { name: 'MD list bullet', scope: ['punctuation.definition.list.begin.markdown'], settings: { foreground: t.accent } },

    // Diff / patch
    { name: 'Diff inserted', scope: ['markup.inserted'], settings: { foreground: t.accent } },
    { name: 'Diff deleted', scope: ['markup.deleted'], settings: { foreground: t.red } },
    { name: 'Diff changed', scope: ['markup.changed'], settings: { foreground: t.accentAlt } },
    { name: 'Diff header and range', scope: ['meta.diff.header', 'meta.diff.range'], settings: { foreground: t.textMuted } },
  ];
}

// Semantic tokens mirror the TextMate scheme (design doc table).
// Values are plain color strings — no fontStyle objects.
function semanticTokenColors(t) {
  return {
    namespace: t.textNormal,
    class: t.accentAlt,
    enum: t.accentAlt,
    interface: t.accentAlt,
    struct: t.accentAlt,
    type: t.accentAlt,
    typeParameter: t.accentAlt,
    function: t.accentAlt,
    method: t.accentAlt,
    decorator: t.accentAlt,
    macro: t.violet,
    keyword: t.violet,
    modifier: t.violet,
    number: t.orange,
    regexp: t.orange,
    enumMember: t.orange,
    boolean: t.orange,
    string: t.accent,
    comment: t.codeComment,
    operator: t.textSoft,
    property: t.warm,
    variable: t.textNormal,
    parameter: t.textNormal,
  };
}

module.exports = { tokenColors, semanticTokenColors };
