import os
import shutil

FOLDERS_TO_DELETE = ["bin", "obj"]

EXTENSIONS_TO_DELETE = [
    ".user",        
    ".vspscc",      
    ".vssscc",
    ".cache",       
    ".log",         
    ".wr"
]


def delete_unwanted_items_dotnet(directory, extensions, folders):
    print(f"Начинаем очистку C# проекта в директории: {directory}")

    for root, dirs, files in os.walk(directory, topdown=True):
        
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"🗑️ Удалён служебный файл: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка при удалении файла {file_path}: {e}")
        
        dirs_to_remove = []
        for folder in folders:
            if folder in dirs:
                folder_path = os.path.join(root, folder)
                try:
                    shutil.rmtree(folder_path)
                    print(f"🗑️ Удалена папка сборки: {folder_path}")
                    
                    dirs_to_remove.append(folder)
                except Exception as e:
                    print(f"❌ Ошибка при удалении папки {folder_path}: {e}")
        
        for folder in dirs_to_remove:
            dirs.remove(folder)



project_path  = input("Введите путь к папке с проектом: ")

delete_unwanted_items_dotnet(project_path, EXTENSIONS_TO_DELETE, FOLDERS_TO_DELETE)

print("\nОчистка C# проекта завершена! Репозиторий готов к загрузке на GitHub.")