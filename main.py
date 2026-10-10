from src.scanner import scan_duplicates
from src.analyzer import analyze_duplicates

def main():
    print("========== AI 文件管家启动 ==========")
    
    # 第一步：扫描重复文件，拿到列表
    duplicate_files = scan_duplicates()
    
    # 第二步：把列表交给 AI 分析
    if duplicate_files:
        ai_suggestion = analyze_duplicates(duplicate_files)
        
        print("\n========== AI 分析报告 ==========")
        print(ai_suggestion)
        print("===================================")
    else:
        print("没有找到重复文件，程序结束。")

if __name__ == "__main__":
    main()