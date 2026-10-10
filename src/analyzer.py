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

        # 让 AI 只输出一个最应该保留的完整路径
    prompt = f"""
    你是一个专业的文件管家。我通过哈希算法发现以下几个文件的内容是 100% 完全相同的：
    {file_paths}
    
    请从中选择一个最应该保留的文件（比如名字最规范、没有多余后缀的）。
    只输出它的完整路径，不要输出任何其他的解释文字，也不要加引号。
    """
    
    print("\n正在呼叫 AI 分析中，请稍候...")
    
    try:
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {"role": "system", "content": "你是一个专业的AI文件管家。"},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        # 去掉 AI 可能会加上的空格
        result = response.choices[0].message.content.strip()
        return result
        
    except Exception as e:
        return f"AI 分析失败，报错信息：{e}"