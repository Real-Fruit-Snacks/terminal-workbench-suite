" twb-dark - Terminal Workbench dark
" Port of https://github.com/Real-Fruit-Snacks/terminal-workbench-suite
" Calm graphite surfaces, restrained ANSI-style accents.

set background=dark
highlight clear
if exists('syntax_on')
  syntax reset
endif
let g:colors_name = 'twb-dark'

let s:p = {}
" Surfaces
let s:p.bg0            = ['#090c0d', 232]
let s:p.bg1            = ['#0e1214', 233]
let s:p.bg2            = ['#13191c', 234]
let s:p.bg3            = ['#182024', 234]
let s:p.bg4            = ['#202a2f', 235]  " reserved: highest raised surface, kept for palette completeness
let s:p.border         = ['#2a363d', 236]
let s:p.border_strong  = ['#39484f', 238]
" Text
let s:p.text_normal    = ['#dce4df', 254]
let s:p.text_soft      = ['#b4c3bd', 250]
let s:p.text_muted     = ['#879994', 246]
let s:p.text_faint     = ['#63736f', 242]
let s:p.text_on_accent = ['#07100d', 232]
" Accents
let s:p.accent         = ['#63f2ab', 85]
let s:p.accent_alt     = ['#6bdcff', 81]
let s:p.warm           = ['#f0c674', 222]
let s:p.red            = ['#ff6e7a', 204]
let s:p.orange         = ['#f7a35c', 215]
let s:p.violet         = ['#b78cff', 141]
" Derived tints (mix(source, bg0, pct) precomputed per the design system)
let s:p.visual         = ['#204634', 236]
let s:p.search_bg      = ['#264a56', 238]
let s:p.diff_add       = ['#162e25', 235]
let s:p.diff_delete    = ['#2e1b1d', 235]
let s:p.diff_change    = ['#15252a', 235]
let s:p.diff_text      = ['#2b5562', 239]
let s:p.todo_bg        = ['#2c281c', 235]
" :terminal slot aliases
let s:p.ansi_black        = s:p.bg0
let s:p.ansi_white        = s:p.text_soft
let s:p.ansi_bright_white = s:p.text_normal

call twb#apply(s:p)
