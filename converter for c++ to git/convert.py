import os
import shutil

def delete_unwanted_items(directory, extensions, folder_to_remove):
    for root, dirs, files in os.walk(directory):
        # Удаление файлов с определёнными расширениями
        for file in files:
            if file.endswith(tuple(extensions)):  
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Удалён файл: {file_path}")
                except Exception as e:
                    print(f"Ошибка при удалении файла {file_path}: {e}")

        # Удаление папки x64, если она есть
        if folder_to_remove in dirs:
            folder_path = os.path.join(root, folder_to_remove)
            try:
                shutil.rmtree(folder_path)
                print(f"Удалена папка: {folder_path}")
            except Exception as e:
                print(f"Ошибка при удалении папки {folder_path}: {e}")

project_path = "C:/Users/yyhsi/OneDrive/Рабочий стол/KPO/laba_4"

extensions_to_delete = [".filters", ".user"]

folder_to_delete = "x64"

delete_unwanted_items(project_path, extensions_to_delete, folder_to_delete)