# main.py

def input_data():
    # Заглушка для ввода данных
    return "Данные введены."

def execute_algorithm(data):
    # Заглушка для выполнения алгоритма
    return "Алгоритм выполнен."

def display_result(result):
    # Заглушка для отображения результата
    return "Результат отображен."

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
