import os
from openai import OpenAI
from pypdf import PdfReader

# 读取 PDF 里的文字
reader = PdfReader("data.pdf.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

print(f"PDF 读完了，共提取出 {len(text)} 个字符。")

# 调用 AI 总结
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个学习助手，擅长提炼重点，回答要条理清晰。"},
        {"role": "user", "content": f"帮我总结一下这份资料的重点：\n\n{text}"}
    ]
)

print(response.choices[0].message.content)