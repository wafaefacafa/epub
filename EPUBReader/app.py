import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import json

# 配置页面
st.set_page_config(
    page_title="轻小说阅读器",
    page_icon="📚",
    layout="wide"
)

# 标题
st.title("📚 轻小说阅读器")
st.markdown("---")

# 侧边栏 - 搜索选项
with st.sidebar:
    st.header("搜索选项")
    search_type = st.selectbox(
        "选择搜索方式",
        ["编号检索", "作者检索", "书名检索"]
    )
    
    search_query = st.text_input("输入搜索内容")
    search_button = st.button("🔍 搜索")
    
    st.markdown("---")
    st.header("下载选项")
    download_mode = st.radio(
        "选择下载模式",
        ["整本下载", "分卷下载", "图片下载"]
    )

# 主内容区域
col1, col2 = st.columns([2, 1])

with col1:
    st.header("搜索结果")
    
    # 初始化会话状态
    if 'search_results' not in st.session_state:
        st.session_state.search_results = []
    if 'selected_novel' not in st.session_state:
        st.session_state.selected_novel = None
    
    # 搜索功能
    if search_button and search_query:
        with st.spinner("正在搜索..."):
            # 模拟搜索结果（实际应用中应该连接到真实的API或数据库）
            st.session_state.search_results = [
                {
                    "id": f"LN{i+1:04d}",
                    "title": f"{search_query} - 示例小说 {i+1}",
                    "author": f"作者 {i+1}",
                    "volumes": i+5,
                    "status": "连载中" if i % 2 == 0 else "已完结"
                }
                for i in range(5)
            ]
        st.success(f"找到 {len(st.session_state.search_results)} 部作品")
    
    # 显示搜索结果
    if st.session_state.search_results:
        for idx, novel in enumerate(st.session_state.search_results):
            with st.expander(f"📖 {novel['title']} ({novel['id']})"):
                col_a, col_b, col_c = st.columns([2, 1, 1])
                with col_a:
                    st.write(f"**作者:** {novel['author']}")
                    st.write(f"**卷数:** {novel['volumes']}")
                    st.write(f"**状态:** {novel['status']}")
                with col_b:
                    if st.button("选择", key=f"select_{idx}"):
                        st.session_state.selected_novel = novel
                        st.rerun()
    else:
        st.info("请使用左侧搜索框搜索轻小说")

with col2:
    st.header("详细信息")
    
    if st.session_state.selected_novel:
        novel = st.session_state.selected_novel
        
        # 显示封面占位符
        st.image("https://via.placeholder.com/300x400?text=封面", use_container_width=True)
        
        st.subheader(novel['title'])
        st.write(f"**编号:** {novel['id']}")
        st.write(f"**作者:** {novel['author']}")
        st.write(f"**卷数:** {novel['volumes']}")
        st.write(f"**状态:** {novel['status']}")
        
        st.markdown("---")
        
        # 下载功能
        st.subheader("开始下载")
        
        if download_mode == "整本下载":
            st.write("将下载所有卷合并为一个EPUB文件")
        elif download_mode == "分卷下载":
            volume_range = st.slider(
                "选择下载卷数",
                1, novel['volumes'],
                (1, novel['volumes'])
            )
            st.write(f"将下载第 {volume_range[0]} 到 {volume_range[1]} 卷")
        else:  # 图片下载
            st.write("将下载小说中的所有插图和封面")
        
        if st.button("🚀 开始使用", type="primary", use_container_width=True):
            with st.spinner("正在处理..."):
                # 模拟下载和转换过程
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                
                # 创建输出目录
                output_dir = Path("output")
                output_dir.mkdir(exist_ok=True)
                
                # 生成示例EPUB文件信息
                filename = f"{novel['title'].replace(' ', '_')}.epub"
                
                st.success("✅ 处理完成！")
                st.info(f"文件已生成: {filename}")
                
                # 提供下载按钮（实际应用中应该提供真实的文件）
                st.download_button(
                    label="📥 下载EPUB文件",
                    data="示例EPUB内容",
                    file_name=filename,
                    mime="application/epub+zip"
                )
    else:
        st.info("请从左侧选择一部作品")

# 底部信息
st.markdown("---")
st.markdown("""
### 功能说明
- **多维度检索**: 支持通过编号、作者、书名搜索
- **下载功能**: 支持整本、分卷、图片下载
- **格式转换**: 自动生成标准EPUB格式文件

### 使用流程
1. 在左侧选择搜索方式并输入关键词
2. 点击搜索按钮查找作品
3. 从搜索结果中选择目标作品
4. 在右侧选择下载模式
5. 点击"开始使用"生成并下载EPUB文件
""")

# 页脚
st.caption("轻小说阅读器 - 基于Streamlit构建")
