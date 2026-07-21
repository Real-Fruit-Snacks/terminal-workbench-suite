// Terminal Workbench
// https://github.com/Real-Fruit-Snacks/terminal-workbench-suite

import { EditorView } from '@codemirror/view';
import { HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { tags } from '@lezer/highlight';

export const terminalWorkbenchDarkTheme = EditorView.theme(
  {
    '&': {
      color: '#b4c3bd',
      backgroundColor: '#090c0d',
    },
    '.cm-content': {
      caretColor: '#63f2ab',
    },
    '.cm-cursor': {
      borderLeftColor: '#63f2ab',
    },
    '.cm-activeLine': {
      backgroundColor: '#13191c',
    },
    '.cm-gutters': {
      backgroundColor: '#090c0d',
      color: '#63736f',
    },
    '.cm-activeLineGutter': {
      color: '#b4c3bd',
    },
    '.cm-selectionBackground, &.cm-focused .cm-selectionBackground': {
      backgroundColor: '#204634',
    },
    '.cm-searchMatch': {
      backgroundColor: '#264a56',
    },
    '.cm-panels': {
      backgroundColor: '#0e1214',
    },
    '.cm-tooltip': {
      backgroundColor: '#0e1214',
      border: '1px solid #2a363d',
    },
  },
  { dark: true }
);

export const terminalWorkbenchLightTheme = EditorView.theme(
  {
    '&': {
      color: '#34443f',
      backgroundColor: '#f5f7f4',
    },
    '.cm-content': {
      caretColor: '#007a4d',
    },
    '.cm-cursor': {
      borderLeftColor: '#007a4d',
    },
    '.cm-activeLine': {
      backgroundColor: '#e2eae5',
    },
    '.cm-gutters': {
      backgroundColor: '#f5f7f4',
      color: '#81918a',
    },
    '.cm-activeLineGutter': {
      color: '#34443f',
    },
    '.cm-selectionBackground, &.cm-focused .cm-selectionBackground': {
      backgroundColor: '#b8d8ca',
    },
    '.cm-searchMatch': {
      backgroundColor: '#acceda',
    },
    '.cm-panels': {
      backgroundColor: '#edf2ee',
    },
    '.cm-tooltip': {
      backgroundColor: '#edf2ee',
      border: '1px solid #bfcbc5',
    },
  },
  { dark: false }
);

export const terminalWorkbenchDarkHighlight = HighlightStyle.define([
  { tag: tags.comment, color: '#879994' },
  { tag: tags.string, color: '#63f2ab' },
  { tag: tags.escape, color: '#6bdcff' },
  { tag: tags.regexp, color: '#f7a35c' },
  { tag: tags.keyword, color: '#b78cff' },
  { tag: tags.operator, color: '#b4c3bd' },
  { tag: tags.function(tags.variableName), color: '#6bdcff' },
  { tag: [tags.typeName, tags.className], color: '#6bdcff' },
  { tag: [tags.number, tags.bool, tags.atom], color: '#f7a35c' },
  { tag: tags.propertyName, color: '#f0c674' },
  { tag: tags.attributeName, color: '#f0c674' },
  { tag: tags.tagName, color: '#ff6e7a' },
  { tag: tags.heading, color: '#63f2ab', fontWeight: 'bold' },
  { tag: tags.link, color: '#6bdcff' },
  { tag: tags.invalid, color: '#ff6e7a' },
]);

export const terminalWorkbenchLightHighlight = HighlightStyle.define([
  { tag: tags.comment, color: '#60706a' },
  { tag: tags.string, color: '#007a4d' },
  { tag: tags.escape, color: '#006f9e' },
  { tag: tags.regexp, color: '#b65800' },
  { tag: tags.keyword, color: '#7357b8' },
  { tag: tags.operator, color: '#34443f' },
  { tag: tags.function(tags.variableName), color: '#006f9e' },
  { tag: [tags.typeName, tags.className], color: '#006f9e' },
  { tag: [tags.number, tags.bool, tags.atom], color: '#b65800' },
  { tag: tags.propertyName, color: '#a46600' },
  { tag: tags.attributeName, color: '#a46600' },
  { tag: tags.tagName, color: '#c8324c' },
  { tag: tags.heading, color: '#007a4d', fontWeight: 'bold' },
  { tag: tags.link, color: '#006f9e' },
  { tag: tags.invalid, color: '#c8324c' },
]);

export const terminalWorkbenchDark = [
  terminalWorkbenchDarkTheme,
  syntaxHighlighting(terminalWorkbenchDarkHighlight),
];

export const terminalWorkbenchLight = [
  terminalWorkbenchLightTheme,
  syntaxHighlighting(terminalWorkbenchLightHighlight),
];
