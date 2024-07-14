from pathlib import Path

def get_cats_info(path):
    # Функція читає файл та повертає список словників з інформацією про кожного кота
    path = Path(path)
    try:
        with open(file=path, mode='r', encoding='utf-8') as cats_info:
            lines_strip = [elem.strip() for elem in cats_info]
            string_split = [line.split(',') for line in lines_strip]
            result_list = [{"id": item[0], "name": item[1], "age": item[2]} for item in string_split]                    
            return result_list
    except Exception as e:
        print(f"Unexpected error appeared: {e}")

cats_info = get_cats_info("Task_2\cats_info.txt")
print(cats_info)