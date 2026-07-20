'use strict';

function parseHex(hex) {
  const h = hex.replace('#', '');
  return [
    parseInt(h.slice(0, 2), 16),
    parseInt(h.slice(2, 4), 16),
    parseInt(h.slice(4, 6), 16),
  ];
}

function toHex(r, g, b) {
  const c = (n) => Math.round(Math.max(0, Math.min(255, n))).toString(16).padStart(2, '0');
  return `#${c(r)}${c(g)}${c(b)}`;
}

// 8-digit hex from a 6-digit hex + alpha fraction: alpha('#63f2ab', 0.2) === '#63f2ab33'
function alpha(hex, fraction) {
  const a = Math.round(fraction * 255).toString(16).padStart(2, '0');
  return `${hex.toLowerCase()}${a}`;
}

// Blend b into a by weight 0..1: mix('#000000', '#ffffff', 0.5) === '#808080'
function mix(a, b, weight) {
  const [ar, ag, ab] = parseHex(a);
  const [br, bg, bb] = parseHex(b);
  return toHex(ar + (br - ar) * weight, ag + (bg - ag) * weight, ab + (bb - ab) * weight);
}

function lighten(hex, f) { return mix(hex, '#ffffff', f); }
function darken(hex, f) { return mix(hex, '#000000', f); }

// WCAG 2.x relative luminance
function luminance(hex) {
  const [r, g, b] = parseHex(hex).map((c) => {
    const s = c / 255;
    return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

// WCAG contrast ratio, always >= 1
function contrast(a, b) {
  const la = luminance(a);
  const lb = luminance(b);
  const hi = Math.max(la, lb);
  const lo = Math.min(la, lb);
  return (hi + 0.05) / (lo + 0.05);
}

module.exports = { parseHex, alpha, mix, lighten, darken, luminance, contrast };
