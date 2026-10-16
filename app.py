import os
import gradio as gr
from openai import OpenAI
from pypdf import PdfReader

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def answer_pdf(pdf_file, question):
    # 读取 PDF
    reader = PdfReader(pdf_file.name)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # 问 AI
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个学习助手，根据用户提供的资料回答问题。"},
            {"role": "user", "content": f"资料内容：\n\n{text}\n\n问题：{question}"}
        ]
    )
    return response.choices[0].message.content

# 搭界面
demo = gr.Interface(
    fn=answer_pdf,
    inputs=[
        gr.File(label="上传 PDF"),
        gr.Textbox(label="你的问题")
    ],
    outputs=gr.Textbox(label="AI 的回答"),
    title="PDF 问答助手"
)

demo.launch()