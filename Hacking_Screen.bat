@echo off
setlocal enabledelayedexpansion
color 02

:loop
rem Pick how many random numbers to print on this line (1–30)
set /a count=%random% %% 30 + 1

set line=
for /l %%i in (1,1,%count%) do (
    set line=!line! !random!
)

echo !line!
goto loop
