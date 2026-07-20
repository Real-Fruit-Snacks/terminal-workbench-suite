'use strict';

const { alpha, mix } = require('./lib/color');

// ANSI palette (design doc). Bright variants: mix 12% toward white in
// dark mode, toward black in light mode. Light-mode black/white are
// remapped to inks — ANSI black is a foreground color and light bg4
// would be invisible on light surfaces.
function terminalColors(t, isDark) {
  const bright = (hex) => (isDark ? mix(hex, '#ffffff', 0.12) : mix(hex, '#000000', 0.12));
  return {
    'terminal.background': t.bg0,
    'terminal.foreground': t.textSoft,
    'terminal.border': t.border,
    'terminal.selectionBackground': alpha(t.accent, isDark ? 0.2 : 0.17),
    'terminal.inactiveSelectionBackground': alpha(t.accent, isDark ? 0.1 : 0.085),
    'terminalCursor.foreground': t.accent,
    'terminalCursor.background': t.textOnAccent,
    'terminal.ansiBlack': isDark ? t.bg4 : t.textNormal,
    'terminal.ansiBrightBlack': isDark ? t.textFaint : t.textSoft,
    'terminal.ansiRed': t.red,
    'terminal.ansiBrightRed': bright(t.red),
    'terminal.ansiGreen': t.accent,
    'terminal.ansiBrightGreen': bright(t.accent),
    'terminal.ansiYellow': t.warm,
    'terminal.ansiBrightYellow': bright(t.warm),
    'terminal.ansiBlue': t.ansiBlue,
    'terminal.ansiBrightBlue': bright(t.ansiBlue),
    'terminal.ansiMagenta': t.violet,
    'terminal.ansiBrightMagenta': bright(t.violet),
    'terminal.ansiCyan': t.accentAlt,
    'terminal.ansiBrightCyan': bright(t.accentAlt),
    'terminal.ansiWhite': isDark ? t.textSoft : t.textMuted,
    'terminal.ansiBrightWhite': isDark ? t.textNormal : t.textFaint,
  };
}

module.exports = { terminalColors };
