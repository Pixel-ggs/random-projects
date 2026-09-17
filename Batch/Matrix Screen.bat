@echo off
setlocal enabledelayedexpansion
color 02

:loop
set /a count=%random% %% 30 + 1

set line=
for /l %%i in (1,1,%count%) do (
    set line=!line! !random!
)

echo !line!
goto loop

rem rarely use ts language, funny lil matrix screen
