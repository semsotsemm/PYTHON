import os
import shutil

EXTENSIONS_TO_DELETE = [
    ".filters", ".user", 
    ".ipch", ".obj", ".exe", ".pdb", 
    ".ilk", ".tlog", ".lastbuildstate", 
    ".log", ".bin"
]

FOLDERS_TO_DELETE = ["x64", "Debug", "Release", "ipch"]


def delete_files_by_extension(directory, extensions):
    print(f"Начинаем удаление файлов в {directory}...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)): 
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"🗑️ Удалён файл: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка при удалении файла {file_path}: {e}")
                    

def delete_specific_folders(directory, folders):
    print(f"\nНачинаем удаление папок в {directory}...")
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs_to_remove = []
        for folder in dirs:
            if folder in folders:
                folder_path = os.path.join(root, folder)
                try:
                    shutil.rmtree(folder_path)
                    print(f"🗑️ Удалена папка: {folder_path}")
                    dirs_to_remove.append(folder)
                except Exception as e:
                    print(f"❌ Ошибка при удалении папки {folder_path}: {e}")
        
        for folder in dirs_to_remove:
            dirs.remove(folder)

project_path  = input("Введите путь к папке с проектом: ")

delete_files_by_extension(project_path, EXTENSIONS_TO_DELETE)
delete_specific_folders(project_path, FOLDERS_TO_DELETE)

print("\nОчистка проекта завершена! Теперь можно безопасно загружать на GitHub.")