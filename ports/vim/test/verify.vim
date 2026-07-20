" Verifies key highlight groups against the spec palette values.
set nocompatible
set runtimepath+=.
let s:fails = []

function! s:Check(group, what, expected) abort
  call s:CheckMode(a:group, a:what, 'gui', a:expected)
endfunction

function! s:CheckMode(group, what, mode, expected) abort
  let l:actual = synIDattr(synIDtrans(hlID(a:group)), a:what, a:mode)
  if tolower(l:actual) !=# tolower(a:expected)
    call add(s:fails, g:colors_name . ': ' . a:group . ' ' . a:what
          \ . ' (' . a:mode . ')="' . l:actual . '" want "' . a:expected . '"')
  endif
endfunction

function! s:CheckNotItalic(group) abort
  let l:actual = synIDattr(synIDtrans(hlID(a:group)), 'italic', 'gui')
  if l:actual ==# '1'
    call add(s:fails, g:colors_name . ': ' . a:group . ' italic (gui)="1" want not "1"')
  endif
endfunction

try
  colorscheme twb-dark
  call s:Check('Normal',    'fg', '#dce4df')
  call s:Check('Normal',    'bg', '#090c0d')
  call s:Check('Comment',   'fg', '#879994')
  call s:Check('Statement', 'fg', '#b78cff')
  call s:Check('String',    'fg', '#f7a35c')
  call s:Check('Function',  'fg', '#6bdcff')
  call s:Check('Type',      'fg', '#63f2ab')
  call s:Check('Visual',    'bg', '#204634')
  call s:Check('IncSearch', 'bg', '#63f2ab')
  call s:Check('Search',    'bg', '#264a56')
  call s:Check('Todo',      'bg', '#2c281c')
  if get(g:, 'terminal_ansi_colors', [''])[2] !=? '#63f2ab'
    call add(s:fails, 'twb-dark: terminal_ansi_colors[2] != accent')
  endif
  " cterm spot-checks
  call s:CheckMode('Normal',     'fg', 'cterm', '254')
  call s:CheckMode('Statement',  'fg', 'cterm', '141')
  call s:CheckMode('CursorLine', 'bg', 'cterm', '233')
  call s:CheckMode('Visual',     'bg', 'cterm', '236')
  " default-leak regression (Fix 1): unset slots must not inherit Vim defaults
  call s:CheckMode('Error',    'bg', 'gui', '')
  call s:CheckMode('Conceal',  'bg', 'gui', '')
  call s:CheckMode('ErrorMsg', 'bg', 'gui', '')
  " italics sweep: no italics anywhere
  for s:g in ['Comment', 'String', 'Keyword', 'Function', 'Type', 'Identifier', 'Todo']
    call s:CheckNotItalic(s:g)
  endfor
catch
  call add(s:fails, 'twb-dark: EXCEPTION ' . v:exception)
endtry

try
  colorscheme twb-light
  call s:Check('Normal',    'fg', '#17201d')
  call s:Check('Normal',    'bg', '#f5f7f4')
  call s:Check('Comment',   'fg', '#60706a')
  call s:Check('Statement', 'fg', '#7357b8')
  call s:Check('String',    'fg', '#b65800')
  call s:Check('Function',  'fg', '#006f9e')
  call s:Check('Type',      'fg', '#007a4d')
  call s:Check('Visual',    'bg', '#b8d8ca')
  call s:Check('IncSearch', 'bg', '#007a4d')
  call s:Check('Search',    'bg', '#acceda')
  call s:Check('Todo',      'bg', '#e9e1cf')
  if get(g:, 'terminal_ansi_colors', [''])[2] !=? '#007a4d'
    call add(s:fails, 'twb-light: terminal_ansi_colors[2] != accent')
  endif
  " cterm spot-checks
  call s:CheckMode('Normal',     'fg', 'cterm', '234')
  call s:CheckMode('Statement',  'fg', 'cterm', '61')
  call s:CheckMode('CursorLine', 'bg', 'cterm', '254')
  call s:CheckMode('Visual',     'bg', 'cterm', '151')
  " default-leak regression (Fix 1): unset slots must not inherit Vim defaults
  call s:CheckMode('Error',    'bg', 'gui', '')
  call s:CheckMode('Conceal',  'bg', 'gui', '')
  call s:CheckMode('ErrorMsg', 'bg', 'gui', '')
  " italics sweep: no italics anywhere
  for s:g in ['Comment', 'String', 'Keyword', 'Function', 'Type', 'Identifier', 'Todo']
    call s:CheckNotItalic(s:g)
  endfor
catch
  call add(s:fails, 'twb-light: EXCEPTION ' . v:exception)
endtry

call writefile(empty(s:fails) ? ['OK'] : s:fails, 'test/result-verify.txt')
qa!
