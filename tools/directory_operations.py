import os

def get_current_files() -> list[str]:
    """
    get current files
    return:
        current files list
    """
    current_dir = os.getcwd()
    files = []
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isfile(item_path):
            files.append(item)
    return files

def get_file_content(file_path) -> str:
    """
    get file content
    params:
        file_path: file path
    return:
        file content
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"读取文件失败：{str(e)}"
