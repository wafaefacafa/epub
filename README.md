# 轻小说阅读器 (Light Novel Reader)

这是一个基于Streamlit开发的轻小说阅读器，提供可视化的网页操作界面。

## 快速开始

### Windows用户
双击运行 `run.ps1` 脚本，或在PowerShell中执行：
```powershell
.\run.ps1
```

### Linux/Mac用户
在终端中执行：
```bash
./run.sh
```

### 手动启动
```bash
cd EPUBReader
pip install -r requirements.txt
streamlit run app.py
```

应用将在浏览器中自动打开（默认地址：http://localhost:8501）

## 功能特性

- **多维度检索**: 支持通过编号、作者、书名搜索轻小说
- **整本下载**: 将完整小说保存为单一EPUB文件
- **分卷下载**: 支持按卷单独下载
- **图片下载**: 提取并保存小说中的插图或封面
- **格式转换**: 生成标准EPUB格式文件，适配电子书阅读器

## 详细文档

查看 [EPUBReader/README.md](EPUBReader/README.md) 了解更多信息。

---

### 多语言说明

**English**: This is a light novel reader (fixed version) built with Streamlit. Run `run.ps1` (Windows) or `run.sh` (Linux/Mac) to start. The application provides a visual web interface for searching, downloading, and converting light novels to EPUB format.

**日本語**: これはStreamlitで構築されたライトノベルリーダー（修正版）です。`run.ps1`（Windows）または`run.sh`（Linux/Mac）を実行して起動します。アプリケーションは、ライトノベルの検索、ダウンロード、EPUB形式への変換のためのビジュアルWebインターフェースを提供します。

**Русский**: Это читалка легких романов (исправленная версия), построенная с помощью Streamlit. Запустите `run.ps1` (Windows) или `run.sh` (Linux/Mac) для запуска. Приложение предоставляет визуальный веб-интерфейс для поиска, загрузки и конвертации легких романов в формат EPUB.

**Français**: Ceci est un lecteur de light novels (version corrigée) construit avec Streamlit. Exécutez `run.ps1` (Windows) ou `run.sh` (Linux/Mac) pour démarrer. L'application fournit une interface web visuelle pour rechercher, télécharger et convertir des light novels au format EPUB.

**Deutsch**: Dies ist ein Light-Novel-Leseprogramm (korrigierte Version), das mit Streamlit erstellt wurde. Führen Sie `run.ps1` (Windows) oder `run.sh` (Linux/Mac) aus, um zu starten. Die Anwendung bietet eine visuelle Weboberfläche zum Suchen, Herunterladen und Konvertieren von Light Novels in das EPUB-Format.
