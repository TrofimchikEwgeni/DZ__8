filename_work = "phon.txt"

def work_with_phonebook():

    choice = show_menu()

    phone_book = read_txt(filename_work)

    while choice != 8:

        if choice == 1: #"1. Отобразить весь справочник\n"
            print_result(phone_book)
        elif choice == 2: #"2. Найти абонента по фамилии\n"
            last_name = input("Фамилия: ")
            print(find_by_lastname(phone_book,last_name))
            input("Press Enter to continue...")
        elif choice == 3: #"3. Найти абонента по номеру телефона\n"
            number = input("Номер телефона: ")
            if number.isdigit():
                print(find_by_number(phone_book, number))
            else:
                print("Для поиска по номеру телефона необходимо ввести цифры")
            input("Press Enter to continue...")	
        elif choice == 4: #"4. Добавить абонента в справочник/изменить данные\n"
            user_data = input("Введите данные через запятую (Фамилия,Имя,Телефон,Описание): ")
            add_or_change_user(phone_book, user_data)
            write_txt(filename_work, phone_book)
            print("Данные успешно добавлены/изменены")
            input("Press Enter to continue...")	
        elif choice == 5: # Удалить абонента по фамилии
            lastname=input("Фамилия")
            print(delete_by_lastname(phone_book,lastname))
            print("Данные удалены")
            input("Press Enter to continue...")	
        elif choice == 6: # Сохранить данные в файл
            write_txt(filename_work, phone_book)
            print("Данные записаны")
            input("Press Enter to continue...")	
        elif choice == 7: #"7. Скопировать данные в другой файл"
            line_number = int(input("Введите номер строки для копирования:"))
            filename_destination = input("Введите имя файла назначения:")
            copy_line_to_file(phone_book, line_number, filename_destination)
            print("Данные скопированы")
            input("Press Enter to continue...")
        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник/изменить данные\n"
          "5. Удалить абонента по фамилии\n"
          "6. Сохранить данные в файл\n"
          "7. Скопировать данные в другой файл")
    choice = int(input())
    return choice

# -----------Чтение файла

def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename_work, "r", encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(",")))
            clean_record = {key: value.strip() for key, value in record.items()}
            if clean_record["Фамилия"].strip() !="":
                phone_book.append(clean_record)
    return phone_book            
    
#-------------- Запись файла

def write_txt(filename_work, phone_book):
    with open(filename_work,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

#-----------Печать справочника

def print_result(phone_book):
    if not phone_book:
        print("Справочник пуст")
    else:
        print("Справочник:\n")
    i = 0
    for item in phone_book:
        i += 1
        print(
            i,
            item["Фамилия"].ljust(20),
            item["Имя"].ljust(20),
            item["Телефон"].ljust(20),
            item["Описание"].ljust(20)
        )
    input("Press Enter to continue...")	

#-----------Поиск по фамилии

def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i].get("Фамилия", "Нет фамилии") == last_name:
            return phone_book[i]
    return "Не найден"

#--------------Поиск по номеру телефона

def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i].get("Телефон", "Нет номера") == number:
            return phone_book[i]
    return "Не найден"    
    
#------------------Добавить/изменить пользователя

def add_or_change_user(phone_book, user_data):
    fields = user_data.split(",")
    fields = [item.strip() for item in fields]
    print(f"\nДобавляем запись: {fields}")   
    if len(fields) != 4 or not fields[2].isdigit():
        print("Неверный формат ввода")
        return
    
    new_entry = dict(zip(["Фамилия", "Имя", "Телефон", "Описание"], fields))
    for i, entry in enumerate(phone_book):
        if entry["Фамилия"] == new_entry["Фамилия"]:
            phone_book[i] = new_entry
            return
    phone_book.append(new_entry)

#------------Удалить по фамилии

def delete_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            del phone_book[i]
            return True
    return False

#--------------Скопировать данные в другой файл

def copy_line_to_file(phone_book, line_number, filename_destination):
    if 1 <= line_number <= len(phone_book):
        entry = phone_book[line_number - 1]
        with open(filename_destination, "a", encoding='utf-8') as file:
            file.write(f"{entry["Фамилия"]},{entry["Имя"]},{entry["Телефон"]},{entry["Описание"]}\n")
    else:
        print("Неправильный номер строки")

work_with_phonebook()