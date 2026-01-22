@echo off
echo 🚀 启动 Prompt Builder 服务器...
echo.
echo 服务器将在 http://localhost:8000 运行
echo 按 Ctrl+C 停止服务器
echo.

cd /d "%~dp0"

REM 检测并启动服务器
where python3 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python3 -m http.server 8000
    goto :end
)

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python -m http.server 8000
    goto :end
)

where npx >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    npx serve -p 8000 -s
    goto :end
)

echo ❌ 未找到 Python 或 Node.js
echo.
echo 请安装以下任意一个：
echo   - Python: https://www.python.org/downloads/
echo   - Node.js: https://nodejs.org/
echo.
echo 或手动运行：
echo   python3 -m http.server 8000
echo   或
echo   npx serve -p 8000
pause
exit /b 1

:end
