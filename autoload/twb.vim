" autoload/twb.vim - shared engine for the twb colorschemes
" Port of https://github.com/Real-Fruit-Snacks/terminal-workbench-design-system
" Palette entries are [gui_hex, cterm_index] pairs.

" See :help use-cpo-save. s:hi/s:spell below use backslash line continuations,
" which are misparsed if 'cpoptions' contains 'C' (e.g. compatible mode).
let s:cpo_save = &cpo
set cpo&vim

" Emit one :highlight command with both gui* and cterm* attributes.
" fg/bg: palette pairs, or the empty list to explicitly clear to NONE.
" attr: '' means explicitly NONE (never inherit stray bold/underline).
function! s:hi(group, fg, bg, attr) abort
  let l:cmd = 'highlight ' . a:group
  if empty(a:fg)
    let l:cmd .= ' guifg=NONE ctermfg=NONE'
  else
    let l:cmd .= ' guifg=' . a:fg[0] . ' ctermfg=' . a:fg[1]
  endif
  if empty(a:bg)
    let l:cmd .= ' guibg=NONE ctermbg=NONE'
  else
    let l:cmd .= ' guibg=' . a:bg[0] . ' ctermbg=' . a:bg[1]
  endif
  let l:attr = empty(a:attr) ? 'NONE' : a:attr
  let l:cmd .= ' gui=' . l:attr . ' cterm=' . l:attr . ' term=' . l:attr
  execute l:cmd
endfunction

" Spell groups: undercurl + guisp in GUI/true-color, plain underline in cterm.
function! s:spell(group, sp) abort
  execute 'highlight ' . a:group
        \ . ' guifg=NONE ctermfg=NONE guibg=NONE ctermbg=NONE'
        \ . ' gui=undercurl cterm=underline term=underline'
        \ . ' guisp=' . a:sp[0]
endfunction

function! twb#apply(p) abort
  let l:p = a:p
  let l:none = []

  " --- Editor chrome (quiet) -------------------------------------------
  call s:hi('Normal',       l:p.text_normal, l:p.bg0, '')
  call s:hi('NonText',      l:p.text_faint,  l:none,  '')
  call s:hi('SpecialKey',   l:p.text_faint,  l:none,  '')
  call s:hi('EndOfBuffer',  l:p.text_faint,  l:none,  '')
  call s:hi('Conceal',      l:p.text_faint,  l:none,  '')
  call s:hi('LineNr',       l:p.text_faint,  l:none,  '')
  call s:hi('FoldColumn',   l:p.text_faint,  l:none,  '')
  call s:hi('CursorLine',   l:none, l:p.bg1, '')
  call s:hi('CursorColumn', l:none, l:p.bg1, '')
  call s:hi('ColorColumn',  l:none, l:p.bg1, '')
  call s:hi('CursorLineNr', l:p.accent, l:none, 'bold')
  call s:hi('SignColumn',   l:none, l:p.bg0, '')
  call s:hi('Folded',       l:p.text_muted, l:p.bg1, '')
  call s:hi('StatusLine',   l:p.text_soft,  l:p.bg2, '')
  call s:hi('StatusLineNC', l:p.text_muted, l:p.bg1, '')
  call s:hi('VertSplit',    l:p.border, l:none, '')
  call s:hi('TabLine',      l:p.text_muted, l:p.bg1, '')
  call s:hi('TabLineFill',  l:none, l:p.bg1, '')
  call s:hi('TabLineSel',   l:p.accent, l:p.bg0, 'bold')
  call s:hi('Pmenu',        l:p.text_normal, l:p.bg2, '')
  call s:hi('PmenuSel',     l:p.text_on_accent, l:p.accent, '')
  call s:hi('PmenuSbar',    l:none, l:p.bg3, '')
  call s:hi('PmenuThumb',   l:none, l:p.border_strong, '')
  call s:hi('WildMenu',     l:p.text_on_accent, l:p.accent, '')
  call s:hi('Directory',    l:p.accent_alt, l:none, '')
  call s:hi('ModeMsg',      l:p.text_soft, l:none, '')
  highlight! link StatusLineTerm   StatusLine
  highlight! link StatusLineTermNC StatusLineNC

  " --- Signal moments (loud) -------------------------------------------
  call s:hi('Cursor',       l:p.text_on_accent, l:p.accent, '')
  highlight! link lCursor Cursor
  call s:hi('Visual',       l:none, l:p.visual, '')
  call s:hi('VisualNOS',    l:none, l:p.visual, '')
  call s:hi('IncSearch',    l:p.text_on_accent, l:p.accent, '')
  call s:hi('Search',       l:p.text_normal, l:p.search_bg, '')
  call s:hi('QuickFixLine', l:p.text_normal, l:p.search_bg, '')
  call s:hi('MatchParen',   l:p.accent_alt, l:p.bg3, 'bold')
  call s:hi('ErrorMsg',     l:p.red,  l:none, 'bold')
  call s:hi('WarningMsg',   l:p.warm, l:none, '')
  call s:hi('MoreMsg',      l:p.accent, l:none, '')
  call s:hi('Question',     l:p.accent, l:none, '')
  call s:hi('Title',        l:p.accent, l:none, 'bold')

  " --- Syntax -----------------------------------------------------------
  call s:hi('Comment',        l:p.text_muted, l:none, '')
  call s:hi('SpecialComment', l:p.text_muted, l:none, '')
  call s:hi('Statement',      l:p.violet, l:none, '')
  call s:hi('Keyword',        l:p.violet, l:none, '')
  call s:hi('Conditional',    l:p.violet, l:none, '')
  call s:hi('Repeat',         l:p.violet, l:none, '')
  call s:hi('Label',          l:p.violet, l:none, '')
  call s:hi('Exception',      l:p.violet, l:none, '')
  call s:hi('PreProc',        l:p.violet, l:none, '')
  call s:hi('Include',        l:p.violet, l:none, '')
  call s:hi('Define',         l:p.violet, l:none, '')
  call s:hi('Macro',          l:p.violet, l:none, '')
  call s:hi('PreCondit',      l:p.violet, l:none, '')
  call s:hi('Constant',       l:p.orange, l:none, '')
  call s:hi('String',         l:p.orange, l:none, '')
  call s:hi('Character',      l:p.orange, l:none, '')
  call s:hi('Number',         l:p.orange, l:none, '')
  call s:hi('Boolean',        l:p.orange, l:none, '')
  call s:hi('Float',          l:p.orange, l:none, '')
  call s:hi('Function',       l:p.accent_alt, l:none, '')
  call s:hi('Identifier',     l:p.text_normal, l:none, '')
  call s:hi('Type',           l:p.accent, l:none, '')
  call s:hi('StorageClass',   l:p.accent, l:none, '')
  call s:hi('Structure',      l:p.accent, l:none, '')
  call s:hi('Typedef',        l:p.accent, l:none, '')
  call s:hi('Special',        l:p.warm, l:none, '')
  call s:hi('SpecialChar',    l:p.warm, l:none, '')
  call s:hi('Tag',            l:p.warm, l:none, '')
  call s:hi('Debug',          l:p.warm, l:none, '')
  call s:hi('Operator',       l:p.text_soft, l:none, '')
  call s:hi('Delimiter',      l:p.text_soft, l:none, '')
  call s:hi('Underlined',     l:p.accent_alt, l:none, 'underline')
  call s:hi('Todo',           l:p.warm, l:p.todo_bg, 'bold')
  call s:hi('Error',          l:p.red, l:none, 'bold')
  call s:hi('Ignore',         l:p.text_faint, l:none, '')

  " --- Diff -------------------------------------------------------------
  call s:hi('DiffAdd',    l:none, l:p.diff_add, '')
  call s:hi('DiffDelete', l:p.text_faint, l:p.diff_delete, '')
  call s:hi('DiffChange', l:none, l:p.diff_change, '')
  call s:hi('DiffText',   l:none, l:p.diff_text, 'bold')
  call s:hi('diffAdded',   l:p.accent, l:none, '')
  call s:hi('diffRemoved', l:p.red, l:none, '')
  call s:hi('diffChanged', l:p.accent_alt, l:none, '')

  " --- Spell ------------------------------------------------------------
  call s:spell('SpellBad',   l:p.red)
  call s:spell('SpellCap',   l:p.accent_alt)
  call s:spell('SpellLocal', l:p.warm)
  call s:spell('SpellRare',  l:p.violet)

  " --- :terminal ANSI palette (GUI/true-color only) ----------------------
  let g:terminal_ansi_colors = [
        \ l:p.ansi_black[0], l:p.red[0],    l:p.accent[0],     l:p.warm[0],
        \ l:p.accent_alt[0], l:p.violet[0], l:p.accent_alt[0], l:p.ansi_white[0],
        \ l:p.text_faint[0], l:p.red[0],    l:p.accent[0],     l:p.warm[0],
        \ l:p.accent_alt[0], l:p.violet[0], l:p.accent_alt[0], l:p.ansi_bright_white[0],
        \ ]
endfunction

let &cpo = s:cpo_save
unlet s:cpo_save
