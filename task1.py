import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    try:
        # Перевірка, чи існує директорія призначення, якщо ні - створити її
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Проходимо по всіх елементах у вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            
            # Якщо це директорія, викликаємо функцію рекурсивно
            if os.path.isdir(item_path):
                copy_files(item_path, dest_dir)
            # Якщо це файл
            else:
                # Отримуємо розширення файлу
                file_ext = os.path.splitext(item)[-1].lower()[1:]  # без крапки
                # Створюємо піддиректорію для цього розширення
                ext_dir = os.path.join(dest_dir, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(item_path, ext_dir)
                
    except Exception as e:
        print(f"Помилка під час копіювання файлів: {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів і сортування за розширенням")
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    
    args = parser.parse_args()

    # Отримуємо абсолютні шляхи
    src_dir = os.path.abspath(args.src_dir)
    dest_dir = os.path.abspath(args.dest_dir)

    # Виконуємо рекурсивне копіювання
    if os.path.exists(src_dir):
        copy_files(src_dir, dest_dir)
        print(f"Файли успішно скопійовані до {dest_dir}")
    else:
        print(f"Директорія {src_dir} не існує!")

if __name__ == "__main__":
    main()
