from pathlib import Path
import sys
from colorama import Fore, Style

def display_directory_structure(directory_path):
    try:
        # Перевірка чи існує вказаний шлях
        if not directory_path.exists():
            print(f"Шлях {directory_path} не існує.")
            return
             
        for item in directory_path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"Директорія: {item.name}")
            else:
                print(Fore.RED + f"Файл: {item.name}")
        
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    try:
        if len(sys.argv) < 2:
            print("Потрібно вказати шлях до директорії в якості аргументу командного рядка.")
            return
        
        directory_path = Path(sys.argv[1])
        display_directory_structure(directory_path)
        
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()
