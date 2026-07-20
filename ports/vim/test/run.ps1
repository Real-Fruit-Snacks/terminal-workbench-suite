$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
Remove-Item test/result-*.txt -ErrorAction SilentlyContinue

vim -N -es -u NONE -i NONE -S test/smoke.vim | Out-Null
vim -N -es -u NONE -i NONE -S test/verify.vim | Out-Null
vim -es -u NONE -i NONE -c "set cpo+=C" -c "set rtp+=." -c "try | colorscheme twb-dark | colorscheme twb-light | call writefile(['OK'],'test/result-cpo.txt') | catch | call writefile(['FAIL ' . v:exception],'test/result-cpo.txt') | endtry" -c "qa!" | Out-Null

$failed = $false
$smoke = Get-Content test/result-smoke.txt
$smoke | ForEach-Object { Write-Host "smoke:  $_" }
if ($smoke.Count -ne 2 -or $smoke[0] -ne 'twb-dark: OK bg=dark' -or $smoke[1] -ne 'twb-light: OK bg=light') { $failed = $true }

$verify = Get-Content test/result-verify.txt
$verify | ForEach-Object { Write-Host "verify: $_" }
if ($verify -ne 'OK') { $failed = $true }

$cpo = Get-Content test/result-cpo.txt
$cpo | ForEach-Object { Write-Host "cpo:    $_" }
if ($cpo -ne 'OK') { $failed = $true }

if ($failed) { Write-Host 'RESULT: FAIL'; exit 1 }
Write-Host 'RESULT: PASS'; exit 0
