# 轻小说阅读器启动脚本 (Windows)

Write-Host "==================================="
Write-Host "轻小说阅读器 (Light Novel Reader)"
Write-Host "==================================="
Write-Host ""

# 检查Python版本
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python版本: $pythonVersion"
} catch {
    Write-Host "✗ 错误: 未找到Python"
    Write-Host "请安装Python 3.8或更高版本"
    Write-Host "下载地址: https://www.python.org/downloads/"
    pause
    exit 1
}

# 检查是否已安装依赖
try {
    $null = python -c "import streamlit" 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Streamlit not installed"
    }
} catch {
    Write-Host ""
    Write-Host "首次运行，正在安装依赖..."
    Set-Location EPUBReader
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ 依赖安装失败"
        pause
        exit 1
    }
    Set-Location ..
    Write-Host "✓ 依赖安装成功"
}

# 启动应用
Write-Host ""
Write-Host "正在启动应用..."
Write-Host "应用将在浏览器中自动打开"
Write-Host "默认地址: http://localhost:8501"
Write-Host ""
Write-Host "按 Ctrl+C 停止应用"
Write-Host "==================================="
Write-Host ""

Set-Location EPUBReader
streamlit run app.py
