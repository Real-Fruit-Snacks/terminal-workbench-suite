" twb-light - Terminal Workbench light
" Port of https://github.com/Real-Fruit-Snacks/terminal-workbench-suite
" Calm graphite surfaces, restrained ANSI-style accents.

set background=light
highlight clear
if exists('syntax_on')
  syntax reset
endif
let g:colors_name = 'twb-light'

let s:p = {}
" Surfaces
let s:p.bg0            = ['#f5f7f4', 255]
let s:p.bg1            = ['#edf2ee', 254]
let s:p.bg2            = ['#e2eae5', 254]
let s:p.bg3            = ['#d6e1db', 253]
let s:p.bg4            = ['#c8d5cf', 252]  " reserved: highest raised surface, kept for palette completeness
let s:p.border         = ['#bfcbc5', 251]
let s:p.border_strong  = ['#9daea7', 248]
" Text
let s:p.text_normal    = ['#17201d', 234]
let s:p.text_soft      = ['#34443f', 237]
let s:p.text_muted     = ['#60706a', 242]
let s:p.text_faint     = ['#81918a', 245]
let s:p.text_on_accent = ['#f9fbf8', 231]
" Accents
let s:p.accent         = ['#007a4d', 29]
let s:p.accent_alt     = ['#006f9e', 25]
let s:p.warm           = ['#a46600', 130]
let s:p.red            = ['#c8324c', 167]
let s:p.orange         = ['#b65800', 130]
let s:p.violet         = ['#7357b8', 61]
" Derived tints (mix(source, bg0, pct) precomputed per the design system)
let s:p.visual         = ['#b8d8ca', 151]
let s:p.search_bg      = ['#acceda', 152]
let s:p.diff_add       = ['#d0e4db', 253]
let s:p.diff_delete    = ['#eed9db', 254]
let s:p.diff_change    = ['#d8e7ea', 254]
let s:p.diff_text      = ['#9fc7d6', 152]
let s:p.todo_bg        = ['#e9e1cf', 253]
" :terminal slot aliases
let s:p.ansi_black        = s:p.text_normal
let s:p.ansi_white        = s:p.bg2
let s:p.ansi_bright_white = s:p.bg0

call twb#apply(s:p)
