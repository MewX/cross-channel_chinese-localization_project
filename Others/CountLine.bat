@echo off
for /f  %%a in ('type %1') do  set /a v+=1
echo Running for %1 ...
echo LineCount: %v%.
pause
