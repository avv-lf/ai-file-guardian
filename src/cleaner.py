import os
import shutil

# 隔离区文件夹名字
QUARANTINE_DIR = "quarantine"

def move_to_quarantine(delete_files):
    """
    将指定的文件移动到隔离区，而不是直接删除。
    delete_files: 要移动的文件路径列表 (List)
    """
    # 1. 如果没有隔离区文件夹，就创建它
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
        print(f"已创建隔离区文件夹：{QUARANTINE_DIR}")

    moved_count = 0
    for filepath in delete_files:
        if not os.path.exists(filepath):
            print(f"文件不存在，跳过：{filepath}")
            continue

        # 2. 构造目标路径：把文件移动到 quarantine 文件夹里
        # os.path.basename 会只取文件名，比如 "test_files\\A.txt" 变成 "A.txt"
        filename = os.path.basename(filepath)
        target_path = os.path.join(QUARANTINE_DIR, filename)

        # 3. 如果隔离区里已经有同名的文件，我们就加个编号避免覆盖
        counter = 1
        while os.path.exists(target_path):
            # 将 "A.txt" 变成 "A_1.txt", "A_2.txt" 等
            name, ext = os.path.splitext(filename)
            target_path = os.path.join(QUARANTINE_DIR, f"{name}_{counter}{ext}")
            counter += 1

        # 4. 核心操作：移动文件
        try:
            shutil.move(filepath, target_path)
            print(f"✅ 已移至隔离区：{filepath} -> {target_path}")
            moved_count += 1
        except Exception as e:
            print(f"移动失败：{filepath}，原因：{e}")

    print(f"\n操作完成，共移动了 {moved_count} 个文件。")
    print(f"如果后悔了，可以去 {QUARANTINE_DIR} 文件夹里找回来。")