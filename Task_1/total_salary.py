from pathlib import Path

def total_salary(path):
    try:
        path = Path(path)
        with open(file=path, mode='r', encoding='utf-8') as salaries:
            lines = [el.strip() for el in salaries]
            salary_list = [int(line.split(',')[1]) for line in lines]
            
            total = sum(salary_list)
            average = total / len(salary_list)
            
            return total, average
    except FileNotFoundError as f:
        print(f"We didn't find such file - {f}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


total, average = total_salary("Task_1\Salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
