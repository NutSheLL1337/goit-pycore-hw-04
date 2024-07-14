from pathlib import Path

'''
    total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

'''


def total_salary(path):
    # Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
    # Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
    path = Path("Salaries.txt")
    try:
          with open(file=path, mode='r', encoding='utf-8', ) as salaries:
            #total
            #average
            lines = [el.strip(',') for el in salaries.readlines()]
            print(lines)
    except FileNotFoundError as f:
        print(f"We didn't find such file - {f}")

total_salary("Salaries.txt")

