# PDF 问答工具
<img width="2343" height="1081" alt="image" src="https://github.com/user-attachments/assets/a1e25afa-9598-4c9f-a561-7bd6cb6cade3" />

## 这个项目是干嘛的
用 Python 读取 PDF 文件，调用 DeepSeek API，让 AI 基于 PDF 内容回答问题。

## 怎么用
1. 安装依赖：pip install openai pypdf
2. 设置环境变量：DEEPSEEK_API_KEY
3. 运行：python read_pdf.py

## 文件说明
- first_call.py：最基础的 API 调用示例
- read_pdf.py：读取 PDF 并让 AI 总结
