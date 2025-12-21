#!/bin/bash
# 轻小说阅读器启动脚本

echo "==================================="
echo "轻小说阅读器 (Light Novel Reader)"
echo "==================================="
echo ""

# 检查Python版本
python_version=$(python3 --version 2>&1)
if [ $? -eq 0 ]; then
    echo "✓ Python版本: $python_version"
else
    echo "✗ 错误: 未找到Python3"
    echo "请安装Python 3.8或更高版本"
    exit 1
fi

# 检查是否已安装依赖
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo ""
    echo "首次运行，正在安装依赖..."
    cd EPUBReader
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "✗ 依赖安装失败"
        exit 1
    fi
    cd ..
    echo "✓ 依赖安装成功"
fi

# 启动应用
echo ""
echo "正在启动应用..."
echo "应用将在浏览器中自动打开"
echo "默认地址: http://localhost:8501"
echo ""
echo "按 Ctrl+C 停止应用"
echo "==================================="
echo ""

cd EPUBReader
streamlit run app.py
