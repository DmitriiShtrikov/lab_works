def read_file(file_name, read_mode='all'):
    try:
        with open(file_name, 'r') as file:
            if read_mode == 'all':
                content = file.read()
                print(content)
            elif read_mode == 'lines':
                for line in file:
                    print(line.strip())
            else:
                print("Неверный режим чтения. Используйте 'all' или 'lines'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")

read_file('example.txt','lines')


def write_to_file():
    user_text = input("Введите текст для записи в файл: ")
    with open('user_input.txt', 'w') as file:
        file.write(user_text)
write_to_file()


def append_to_file():
    user_text = input("Введите текст для добавления в файл: ")
    with open('user_input.txt', 'a') as file:
        file.write(user_text + '\n')
append_to_file()