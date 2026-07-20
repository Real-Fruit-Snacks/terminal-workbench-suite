'use strict';

const { alpha } = require('./lib/color');

const FONT = "'Cascadia Code','Consolas','SF Mono','Menlo',monospace";
const SANS = "'Segoe UI','SF Pro Text',system-ui,sans-serif";

// A type chip at cover scale — same recipe as build/icons.js (hue @13%
// fill, @28% stroke, hue text).
function chip(x, y, hueHex, label) {
  return `<rect x="${x}" y="${y}" width="46" height="22" rx="4" fill="${alpha(hueHex, 0.13)}" stroke="${alpha(hueHex, 0.28)}"/>` +
    `<text x="${x + 23}" y="${y + 15}" text-anchor="middle" font-family="${FONT}" font-size="11" font-weight="600" fill="${hueHex}">${label}</text>`;
}

// README cover, mirroring the Graphite repo's construction: 1200x460
// rounded graphite panel; left column = manifest label, wordmark,
// tagline, mono strip; right column = mock editor window with tabs,
// syntax-colored code, terminal lines, and type chips.
function coverSvg(t) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 460">
<rect x="1" y="1" width="1198" height="458" rx="24" fill="${t.bg0}" stroke="${t.border}" stroke-width="1.5"/>
<text x="66" y="104" font-family="${FONT}" font-size="15" font-weight="600" letter-spacing="2.2" fill="${t.textFaint}">VS CODE THEME · DARK + LIGHT</text>
<text x="64" y="182" font-family="${FONT}" font-size="58" font-weight="600" fill="${t.textNormal}">terminal</text>
<text x="64" y="248" font-family="${FONT}" font-size="58" font-weight="600" fill="${t.textNormal}">workbench</text>
<text x="66" y="304" font-family="${SANS}" font-size="21" fill="${t.textSoft}">Quiet chrome, loud <tspan fill="${t.accent}">signal.</tspan></text>
<text x="66" y="368" font-family="${FONT}" font-size="12.5" font-weight="600" letter-spacing="2" fill="${t.textFaint}">EDITOR · TERMINAL · ICONS · SYNTAX</text>
<rect x="624" y="64" width="512" height="332" rx="14" fill="${t.bg1}" stroke="${t.border}"/>
<circle cx="652" cy="92" r="5.5" fill="${t.red}"/>
<circle cx="672" cy="92" r="5.5" fill="${t.warm}"/>
<circle cx="692" cy="92" r="5.5" fill="${t.accent}"/>
<line x1="624" y1="108" x2="1136" y2="108" stroke="${t.border}"/>
<rect x="640" y="108" width="100" height="32" fill="${t.bg3}"/>
<rect x="640" y="108" width="100" height="2" fill="${t.accent}"/>
<text x="690" y="129" text-anchor="middle" font-family="${FONT}" font-size="12" font-weight="600" fill="${t.accent}">main.ts</text>
<text x="790" y="129" text-anchor="middle" font-family="${FONT}" font-size="12" fill="${t.textMuted}">app.py</text>
<line x1="624" y1="140" x2="1136" y2="140" stroke="${t.border}"/>
<text x="648" y="172" font-family="${FONT}" font-size="13"><tspan fill="${t.violet}">import</tspan><tspan fill="${t.textSoft}"> { </tspan><tspan fill="${t.accentAlt}">pane</tspan><tspan fill="${t.textSoft}"> } </tspan><tspan fill="${t.violet}">from</tspan><tspan fill="${t.accent}"> 'workbench'</tspan></text>
<text x="648" y="196" font-family="${FONT}" font-size="13"><tspan fill="${t.violet}">const</tspan><tspan fill="${t.textSoft}"> session = </tspan><tspan fill="${t.accentAlt}">attach</tspan><tspan fill="${t.textSoft}">(</tspan><tspan fill="${t.orange}">42</tspan><tspan fill="${t.textSoft}">)</tspan></text>
<text x="648" y="220" font-family="${FONT}" font-size="13" fill="${t.codeComment}">// quiet chrome, loud signal</text>
<text x="648" y="244" font-family="${FONT}" font-size="13"><tspan fill="${t.textSoft}">session.</tspan><tspan fill="${t.warm}">theme</tspan><tspan fill="${t.textSoft}"> = </tspan><tspan fill="${t.accent}">'graphite'</tspan></text>
<line x1="624" y1="264" x2="1136" y2="264" stroke="${t.border}"/>
<text x="648" y="292" font-family="${FONT}" font-size="13"><tspan fill="${t.accent}">$</tspan><tspan fill="${t.textSoft}"> npm test</tspan></text>
<text x="648" y="316" font-family="${FONT}" font-size="13"><tspan fill="${t.accentAlt}">PASS</tspan><tspan fill="${t.textSoft}"> 38 tests · </tspan><tspan fill="${t.warm}">2 accepted warnings</tspan></text>
${chip(648, 344, t.accentAlt, 'TS')}
${chip(704, 344, t.accent, 'PY')}
${chip(760, 344, t.textSoft, 'MD')}
</svg>
`;
}

module.exports = { coverSvg };
