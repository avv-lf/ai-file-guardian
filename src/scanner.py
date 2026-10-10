import os
import hashlib

# 目标文件夹路径
TARGET_DIR = "test_files"

def get_file_hash(filepath):
    """
    计算文件的 MD5 (Message Digest Algorithm 5，消息摘要算法第五版) 哈希值。
    """
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(8192)
        while buf:
            hasher.update(buf)
            buf = f.read(8192)
    return hasher.hexdigest()

def scan_duplicates():
    """
    扫描重复文件，返回一个列表 (List)，列表里包含所有重复文件的路径。
    """
    print("开始扫描重复文件...")
    
    if not os.path.exists(TARGET_DIR):
        print(f"错误：找不到 {TARGET_DIR} 文件夹")
        return [] # 返回空列表

    file_hashes = {}
    # 用来存储所有重复文件的集合 (Set)
    # 使用集合是为了自动去重，比如 [A, B] 重复，我们只记录 [A, B] 一次
    duplicate_set = set()

    for root, dirs, files in os.walk(TARGET_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                file_hash = get_file_hash(filepath)
                
                if file_hash in file_hashes:
                    # 发现了重复文件，把原始文件和当前文件都加进去
                    duplicate_set.add(file_hashes[file_hash])
                    duplicate_set.add(filepath)
                else:
                    file_hashes[file_hash] = filepath
                    
            except Exception as e:
                print(f"无法读取文件：{filepath}，原因：{e}")

    # 把集合转成列表返回 (List)
    result_list = list(duplicate_set)
    
    if result_list:
        print(f"扫描完成，一共发现 {len(result_list)} 个重复文件需要分析。")
    else:
        print("扫描完成，没有发现重复文件。")
        
    return result_list

# 如果直接运行这个文件，就测试一下
if __name__ == "__main__":
    found_files = scan_duplicates()
    print("交给 AI 的文件清单：", found_files)