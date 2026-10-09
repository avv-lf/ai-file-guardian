import os
import hashlib

# 修改这里：指向我们刚建的 test_files 文件夹
TARGET_DIR = "test_files"

file_hashes = {}

def get_file_hash(filepath):
    """
    计算文件的 MD5 (Message Digest Algorithm 5，消息摘要算法第五版) 哈希值。
    相当于把文件内容压缩成独一无二的“指纹”。
    """
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(8192)
        while buf:
            hasher.update(buf)
            buf = f.read(8192)
    return hasher.hexdigest()

def scan_duplicates():
    print("开始扫描重复文件...")
    
    # 检查目标文件夹是否存在，避免直接报错崩溃
    if not os.path.exists(TARGET_DIR):
        print(f"错误：找不到 {TARGET_DIR} 文件夹，请先创建它并放入测试文件。")
        return

    for root, dirs, files in os.walk(TARGET_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            try:
                file_hash = get_file_hash(filepath)
                
                if file_hash in file_hashes:
                    print(f"\n【发现重复文件！】")
                    print(f"原始文件：{file_hashes[file_hash]}")
                    print(f"重复文件：{filepath}")
                else:
                    file_hashes[file_hash] = filepath
                    
            except Exception as e:
                print(f"无法读取文件：{filepath}，原因：{e}")

    print("\n扫描完成！")

if __name__ == "__main__":
    scan_duplicates()