// Verifies that every port's 16-color ANSI palette matches the canonical one.
// Usage: node tools/verify-palette.mjs
//
// The canonical palette is whatever ports/vscode emits, since that port is
// generated from the token tables and gated on contrast. Ports that hold the
// palette by hand are checked against it here — this is the check that would
// have caught the light-mode ANSI white/bright-white slots being set to paper
// surfaces (invisible on a light terminal background) instead of inks.
import { readFileSync } from 'node:fs';

const ROLES = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
  'brblack', 'brred', 'brgreen', 'bryellow', 'brblue', 'brmagenta', 'brcyan', 'brwhite'];

const read = p => readFileSync(new URL(`../${p}`, import.meta.url), 'utf8');
const json = p => JSON.parse(read(p));
const lower = s => s.slice(0, 7).toLowerCase();
const d2h = s => '#' + s.split(',').map(n => (+n).toString(16).padStart(2, '0')).join('');

// index-keyed extraction helper: pattern must capture (index, color)
function byIndex(text, re, conv = x => x.toLowerCase()) {
  const out = {};
  for (const m of text.matchAll(re)) out[ROLES[+m[1]]] = conv(m[2]);
  return out;
}
// list extraction: normals then brights
function byList(normals, brights, conv = x => x.toLowerCase()) {
  const out = {};
  normals.forEach((c, i) => { out[ROLES[i]] = conv(c); });
  brights.forEach((c, i) => { out[ROLES[i + 8]] = conv(c); });
  return out;
}

function canonical(mode) {
  const c = json(`ports/vscode/themes/terminal-workbench-${mode}-color-theme.json`).colors;
  const names = ['Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White', 'BrightBlack',
    'BrightRed', 'BrightGreen', 'BrightYellow', 'BrightBlue', 'BrightMagenta', 'BrightCyan', 'BrightWhite'];
  return Object.fromEntries(ROLES.map((r, i) => [r, lower(c['terminal.ansi' + names[i]])]));
}

function collect(mode) {
  const M = mode[0].toUpperCase() + mode.slice(1);
  const ports = {};

  const wt = json('ports/windows-terminal/terminal-workbench.json');
  const scheme = wt.schemes.find(s => /light/i.test(s.name) === (mode === 'light'));
  const wtKeys = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white', 'brightBlack',
    'brightRed', 'brightGreen', 'brightYellow', 'brightBlue', 'brightPurple', 'brightCyan', 'brightWhite'];
  ports['windows-terminal'] = Object.fromEntries(ROLES.map((r, i) => [r, lower(scheme[wtKeys[i]])]));

  const xKeys = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'brightBlack',
    'brightRed', 'brightGreen', 'brightYellow', 'brightBlue', 'brightMagenta', 'brightCyan', 'brightWhite'];
  const xj = json(`ports/xtermjs/terminal-workbench-${mode}.json`);
  ports['xtermjs/json'] = Object.fromEntries(ROLES.map((r, i) => [r, lower(xj[xKeys[i]])]));

  const mjs = read('ports/xtermjs/index.mjs');
  const sect = mjs.slice(mjs.indexOf(`terminalWorkbench${M}`)).split('}')[0];
  const mjsPairs = Object.fromEntries([...sect.matchAll(/(\w+):\s*'(#[0-9a-fA-F]{6})'/g)].map(m => [m[1], m[2]]));
  ports['xtermjs/mjs'] = Object.fromEntries(ROLES.map((r, i) => [r, lower(mjsPairs[xKeys[i]] ?? '')]));

  const zed = json('ports/zed/themes/terminal-workbench.json').themes.find(t => t.appearance === mode).style;
  const zKeys = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black',
    'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white'];
  ports['zed'] = Object.fromEntries(ROLES.map((r, i) => [r, lower(zed['terminal.ansi.' + zKeys[i]])]));

  const lua = read('ports/neovim/lua/twb/palette.lua');
  const ansiBlock = lua.split(`M.${mode}`)[1].split('ansi = {')[1].split('}')[0];
  ports['neovim'] = Object.fromEntries([...ansiBlock.matchAll(/(\w+)\s*=\s*"(#[0-9a-f]{6})"/g)].map(m => [m[1], m[2]]));

  const icls = read(`ports/jetbrains/Terminal Workbench ${M}.icls`);
  const jKeys = ['BLACK_OUTPUT', 'RED_OUTPUT', 'GREEN_OUTPUT', 'YELLOW_OUTPUT', 'BLUE_OUTPUT', 'MAGENTA_OUTPUT',
    'CYAN_OUTPUT', 'GRAY_OUTPUT', 'DARKGRAY_OUTPUT', 'RED_BRIGHT_OUTPUT', 'GREEN_BRIGHT_OUTPUT',
    'YELLOW_BRIGHT_OUTPUT', 'BLUE_BRIGHT_OUTPUT', 'MAGENTA_BRIGHT_OUTPUT', 'CYAN_BRIGHT_OUTPUT', 'WHITE_OUTPUT'];
  ports['jetbrains'] = Object.fromEntries(ROLES.map((r, i) => {
    const m = icls.match(new RegExp(`"CONSOLE_${jKeys[i]}" value="([0-9a-fA-F]{6})"`));
    return [r, m ? '#' + m[1].toLowerCase() : ''];
  }));

  ports['ghostty'] = byIndex(read(`ports/terminals/ghostty/terminal-workbench-${mode}`),
    /palette\s*=\s*(\d+)=(#[0-9a-fA-F]{6})/g);
  ports['kitty'] = byIndex(read(`ports/terminals/kitty/terminal-workbench-${mode}.conf`),
    /color(\d+)\s+(#[0-9a-fA-F]{6})/g);

  const al = read(`ports/terminals/alacritty/terminal-workbench-${mode}.toml`);
  const alNames = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'];
  const alNormal = al.slice(al.indexOf('[colors.normal]'), al.indexOf('[colors.bright]'));
  const alBright = al.slice(al.indexOf('[colors.bright]'));
  ports['alacritty'] = byList(
    alNames.map(n => alNormal.match(new RegExp(`${n}\\s*=\\s*"(#[0-9a-fA-F]{6})"`))?.[1] ?? ''),
    alNames.map(n => alBright.match(new RegExp(`${n}\\s*=\\s*"(#[0-9a-fA-F]{6})"`))?.[1] ?? ''));

  const foot = read(`ports/terminals/foot/terminal-workbench-${mode}.ini`);
  ports['foot'] = byList(
    [...Array(8).keys()].map(i => '#' + foot.match(new RegExp(`regular${i}=([0-9a-fA-F]{6})`))?.[1]),
    [...Array(8).keys()].map(i => '#' + foot.match(new RegExp(`bright${i}=([0-9a-fA-F]{6})`))?.[1]));

  const wez = read(`ports/terminals/wezterm/Terminal Workbench ${M}.toml`);
  const grab = re => [...wez.match(re)[1].matchAll(/"(#[0-9a-fA-F]{6})"/g)].map(m => m[1]);
  ports['wezterm'] = byList(grab(/ansi = \[([\s\S]*?)\]/), grab(/brights = \[([\s\S]*?)\]/));

  const gt = read(`ports/terminals/gnome-terminal/terminal-workbench-${mode}.dconf`);
  const gtAll = [...gt.match(/palette=\[([\s\S]*?)\]/)[1].matchAll(/'(#[0-9a-fA-F]{6})'/g)].map(m => m[1]);
  ports['gnome-terminal'] = byList(gtAll.slice(0, 8), gtAll.slice(8));

  const ko = read(`ports/terminals/konsole/TerminalWorkbench${M}.colorscheme`);
  ports['konsole'] = byList(
    [...Array(8).keys()].map(i => ko.match(new RegExp(`\\[Color${i}\\]\\nColor=([\\d,]+)`))[1]),
    [...Array(8).keys()].map(i => ko.match(new RegExp(`\\[Color${i}Intense\\]\\nColor=([\\d,]+)`))[1]), d2h);

  // PuTTY stores ANSI as Colour6..21, interleaved normal/bright per hue.
  const pu = read(`ports/terminals/putty/terminal-workbench-${mode}.reg`);
  const puPal = {};
  for (let i = 0; i < 16; i++) {
    const m = pu.match(new RegExp(`"Colour${6 + i}"="([\\d,]+)"`));
    if (m) puPal[ROLES[Math.floor(i / 2) + (i % 2 ? 8 : 0)]] = d2h(m[1]);
  }
  ports['putty'] = puPal;

  // vim assembles its palette in vimscript: read the slot order out of the
  // autoload function, then resolve each key (following aliases) against the
  // colorscheme file, so the wiring itself is what gets checked.
  const twb = read('ports/vim/autoload/twb.vim');
  const ansiStart = twb.indexOf('let g:terminal_ansi_colors');
  const order = [...twb.slice(ansiStart, twb.indexOf('endfunction', ansiStart))
    .matchAll(/l:p\.(\w+)\[0\]/g)].map(m => m[1]);
  const vimSrc = read(`ports/vim/colors/twb-${mode}.vim`);
  const direct = Object.fromEntries(
    [...vimSrc.matchAll(/let s:p\.(\w+)\s*=\s*\['(#[0-9a-fA-F]{6})'/g)].map(m => [m[1], m[2].toLowerCase()]));
  const alias = Object.fromEntries(
    [...vimSrc.matchAll(/let s:p\.(\w+)\s*=\s*s:p\.(\w+)\s*$/gm)].map(m => [m[1], m[2]]));
  const resolve = k => direct[k] ?? (alias[k] ? resolve(alias[k]) : '');
  ports['vim'] = Object.fromEntries(ROLES.map((r, i) => [r, resolve(order[i])]));

  const mo = read(`ports/terminals/mobaxterm/terminal-workbench-${mode}.ini`);
  const moNames = ['Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White'];
  ports['mobaxterm'] = byList(
    moNames.map(n => mo.match(new RegExp(`^${n}=([\\d,]+)`, 'm'))[1]),
    moNames.map(n => mo.match(new RegExp(`^Bold${n}=([\\d,]+)`, 'm'))[1]), d2h);

  return ports;
}

let failures = 0;
for (const mode of ['dark', 'light']) {
  const canon = canonical(mode);
  console.log(`\n${mode}: canonical ${ROLES.map(r => canon[r].slice(1)).join(' ')}`);
  for (const [name, pal] of Object.entries(collect(mode))) {
    const bad = ROLES.filter(r => pal[r] !== canon[r])
      .map(r => `${r} ${pal[r] || 'missing'} != ${canon[r]}`);
    if (bad.length) { failures += bad.length; console.log(`  FAIL ${name}: ${bad.join(', ')}`); }
    else console.log(`  ok   ${name}`);
  }
}
if (failures) {
  console.error(`\nPalette drift: ${failures} slot(s) do not match the canonical ANSI palette.`);
  process.exit(1);
}
console.log('\nAll ports match the canonical ANSI palette.');
