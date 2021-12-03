@ECHO OFF
REM 声明采用UTF-8编码
chcp 65001
ECHO 开始编译，请确保dist目录为空，结束会有提示！
ECHO 编译英文主包Building English version......
pyinstaller main.spec
ECHO 编译中文简体包Building Chinese (Simp) version......
pyinstaller main-zhs.spec
ECHO 编译中文繁体包Building Chinese (Simp) version......
pyinstaller main-zht.spec
CD dist
xcopy  .\逐浪字体精灵.exe .\逐浪字体精灵
rename  逐浪字体精灵.exe 逐浪字体精灵_bak.exe
::xcopy /s .\main-zhs\main-zhs.exe.manifest .\main
::RMDIR /S /Q .\main-zhs
::  REN "main" "CJK-character-count-v0.10"
ECHO 恭喜编译完成Build done，按任意键退出!
pause>nul
EXIT