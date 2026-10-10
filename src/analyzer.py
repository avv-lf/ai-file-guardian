import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

def analyze_duplicates(file_paths):
    """
    接收一个包含重复文件路径的列表 (List)，
    让 AI 分析并返回删除建议。
    """
    # 如果列表为空，直接跳过
    if not file_paths:
        return "没有发现重复文件，无需分析。"

    # 构建 Prompt (提示词)
    prompt = f"""
    你是一个专业的文件管家。我通过哈希算法发现以下几个文件的内容是 100% 完全相同的（互为副本）：
    {file_paths}
    
    请在这些文件中，选择一个最值得保留的（比如名字最规范、没有多余后缀的），删除另外的副本。
    请给出明确的保留建议和删除建议，并用中文解释你的理由。请简明扼要。
    """
    
    print("\n正在呼叫 AI 分析中，请稍候...")
    
    try:
        response = client.chat.completions.create(
            model="glm-4-flash",  # 智谱免费模型
            messages=[
                {"role": "system", "content": "你是一个专业的AI文件管家，回答要简明扼要。"},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"AI 分析失败，报错信息：{e}"