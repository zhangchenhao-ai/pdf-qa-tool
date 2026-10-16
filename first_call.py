import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个帮助大学生学习编程的助教，回答简洁，给代码示例。"},
        {"role": "user", "content": "帮我总结一下这段课程描述的重点"}
    ]
)

print(response.choices[0].message.content)  