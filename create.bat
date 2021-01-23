@echo off

set name=%1
set attribute=%2
set pa=%CD%
cd /d %~dp0

rem it will check if the user entered a folder name 
if "%1" == "" (
    rem if there is no name it will print error
    echo "error you did not enter a name for the file"
rem if the user entered a name it will skip the if condition and enter else condition
) else (
    rem if the user want to make a new repo from zero he will only enter the name
    if "%2" == "" (
        python newremote.py %name% %attribute%
    ) else (
        rem if he wants to make a repo from a local file on the pc he will enter 'l' at the end
        if "%2" == "-l" (
            python localrepo.py %name% %pa%
        )
    )
)