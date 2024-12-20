# main.py

import random

def input_data():
    choice = input("Ввести данные вручную (1) или сгенерировать случайно (2)? ")
    if choice == "1":
        n = int(input("Введите размер матрицы (NxN): "))
        matrix = []
        for i in range(n):
            row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split()))
            matrix.append(row)
    elif choice == "2":
        n = int(input("Введите размер матрицы (NxN): "))
        matrix = [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]
    else:
        print("Неверный выбор. Попробуйте снова.")
        return input_data()
    return matrix

def execute_algorithm(matrix):
    if matrix is None:
        return "Ошибка: данные не введены."
    return {"sorted_rows": matrix, "sorted_columns": matrix}

def display_result(results):
    if results is None:
        print("Ошибка: алгоритм не выполнен.")
    else:
        print("Матрица со строками по убыванию среднего арифметического:")
        print(results["sorted_rows"])
        print("Матрица со столбцами по убыванию среднего арифметического:")
        print(results["sorted_columns"])



def main_menu():
    while True:
        print("\nМеню:")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            data = input_data()
            print(data)
        elif choice == "2":
            result = execute_algorithm(None)
            print(result)
        elif choice == "3":
            display_result(None)
        elif choice == "4":
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
