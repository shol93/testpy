import os
import shutil

# 🔧 Укажи путь к флешке или нужной папке
target_path = input("Укажи путь: ")

# 🛑 Подтверждение от пользователя
confirm = input(f"Ты точно хочешь удалить ВСЁ из '{target_path}'? (y/n): ")

if confirm.lower() == 'y':
    # Проверка, существует ли путь
    if not os.path.exists(target_path):
        print(f"❌ Путь не найден: {target_path}")
    else:
        # 🔁 Проход по всем элементам внутри указанной папки
        for item in os.listdir(target_path):
            item_path = os.path.join(target_path, item)

            # 📄 Если это файл — удаляем
            if os.path.isfile(item_path):
                try:
                    os.remove(item_path)
                    print(f"✅ Удалён файл: {item_path}")
                except Exception as e:
                    print(f"❌ Ошибка при удалении файла {item_path}: {e}")

            # 📂 Если это папка — удаляем её вместе с содержимым
            elif os.path.isdir(item_path):
                try:
                    shutil.rmtree(item_path)
                    print(f"✅ Удалена папка: {item_path}")
                except Exception as e:
                    print(f"❌ Ошибка при удалении папки {item_path}: {e}")
else:
    print("Операция отменена.")