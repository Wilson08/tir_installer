@echo off
set arglist=%1
start /wait powershell -Command "Start-Process cmd -ArgumentList '/k %cd%\\chocolatey.cmd ' -Verb RunAs -Wait"
echo success
exit