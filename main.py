from src.scanner import scan_duplicates
from src.analyzer import analyze_duplicates
from src.cleaner import move_to_quarantine

def main():
    print("========== AI 文件管家启动 ==========")
    
    # 1. 扫描重复文件
    duplicate_files = scan_duplicates()
    
    if not duplicate_files:
        print("没有找到重复文件，程序结束。")
        return

    # 2. 让 AI 告诉我们保留哪一个
    file_to_keep = analyze_duplicates(duplicate_files)
    print(f"\nAI 决定保留：{file_to_keep}")

    # 3. 计算哪些文件需要被清理（除了保留的那个，其他的都要移走）
    # 这里用了列表推导式 (List Comprehension)，是 Python(一种编程语言) 的高级技巧
    files_to_delete = [f for f in duplicate_files if f != file_to_keep]

    if not files_to_delete:
        print("没有文件需要移动。")
        return

    # 4. 打印清理计划，并让用户手动确认
    print("\n即将移至隔离区的文件：")
    for f in files_to_delete:
        print(f" - {f}")

    # 5. 请求用户确认（这是安全性关键，绝不能跳过）
    user_input = input("\n是否确认移动这些文件到隔离区？(y/n): ")
    if user_input.lower() == 'y':
        move_to_quarantine(files_to_delete)
    else:
        print("已取消操作，未移动任何文件。")

if __name__ == "__main__":
    main()