" Headless smoke test: loads each colorscheme, records OK or the exception.
set nocompatible
set runtimepath+=.
let s:results = []
for s:scheme in ['twb-dark', 'twb-light']
  try
    execute 'colorscheme' s:scheme
    call add(s:results, s:scheme . ': OK bg=' . &background)
  catch
    call add(s:results, s:scheme . ': FAIL ' . v:exception)
  endtry
endfor
call writefile(s:results, 'test/result-smoke.txt')
qa!
