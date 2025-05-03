# 管理员权限运行此脚本
$installerPath = "$env:TEMP\innosetup.exe"

# 下载安装包
Invoke-WebRequest -Uri "https://files.jrsoftware.org/is/6/innosetup-6.2.2.exe" -OutFile $installerPath

# 静默安装到默认目录
Start-Process $installerPath -ArgumentList "/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /CURRENTUSER" -Wait

# 手动添加环境变量（需要管理员权限）
$innoPath = "C:\Program Files (x86)\Inno Setup 6"
[System.Environment]::SetEnvironmentVariable("Path", "$([System.Environment]::GetEnvironmentVariable('Path', 'Machine'));$innoPath", 'Machine')

# 验证安装路径
if (Test-Path "$innoPath\ISCC.exe") {
    Write-Host "安装成功！请重启PowerShell后执行打包命令"
} else {
    Write-Host "安装失败，请手动检查安装目录"
}