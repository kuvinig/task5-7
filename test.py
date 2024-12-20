# Итерация 2: Основные функции реализованы, вспомогательные заглушки
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

def sort_rows(matrix):
    # Реализация сортировки строк по убыванию среднего арифметического
    return sorted(matrix, key=lambda row: -sum(row) / len(row))

def sort_columns(matrix):
    # Реализация сортировки столбцов по убыванию среднего арифметического
    transposed = list(zip(*matrix))
    sorted_transposed = sorted(transposed, key=lambda col: -sum(col) / len(col))
    return [list(row) for row in zip(*sorted_transposed)]

def execute_algorithm(matrix):
    # Выполнение алгоритма с учетом условий задачи
    if matrix is None:
        return "Ошибка: данные не введены."
    sorted_rows = sort_rows(matrix)
    sorted_columns = sort_columns(sorted_rows)
    return {"sorted_rows": sorted_rows, "sorted_columns": sorted_columns}

def display_result(results):
    # Заглушка для отображения результата
    if results is None:
        print("Ошибка: алгоритм не выполнен.")
    else:
        print("Матрица со строками по убыванию среднего арифметического:")
        for row in results["sorted_rows"]:
            print(row)
        print("\nМатрица со столбцами по убыванию среднего арифметического:")
        for row in results["sorted_columns"]:
            print(row)

def main_menu():
    matrix = None
    results = None
    while True:
        print("\nМеню:")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            matrix = input_data()
            results = None  # Сброс результатов при вводе новых данных
        elif choice == "2":
            results = execute_algorithm(matrix)
        elif choice == "3":
            display_result(results)
        elif choice == "4":
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
