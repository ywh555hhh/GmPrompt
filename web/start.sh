#!/bin/bash

echo "🚀 启动 Prompt Builder 服务器..."
echo ""
echo "服务器将在 http://localhost:8000 运行"
echo "按 Ctrl+C 停止服务器"
echo ""

# 检测系统并启动服务器
if command -v python3 &> /dev/null; then
    cd "$(dirname "$0")"
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    cd "$(dirname "$0")"
    python -m http.server 8000
elif command -v npx &> /dev/null; then
    npx serve -p 8000 -s
else
    echo "❌ 未找到 Python 或 Node.js"
    echo ""
    echo "请安装以下任意一个："
    echo "  - Python: brew install python3"
    echo "  - Node.js: brew install node"
    echo ""
    echo "或手动运行："
    echo "  python3 -m http.server 8000"
    echo "  或"
    echo "  npx serve -p 8000"
    exit 1
fi
