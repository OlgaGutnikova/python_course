from data_create import *

def input_data():
    name = name_data()
    lastname = lastname_data()
    phonenum = phone_data()
    adres = adress_data()
    var = input(f"""В каком формате вы хотите записать данные?
                         1 вариант:
                         {lastname}, 
                         {name}, 
                         {phonenum}, 
                         {adres}
                         2 вариант: {lastname}; {name}; {phonenum}; {adres}
                         Введите номер варианта: """)
    while var not in ("1", "2"):
        print("Вваринт не верный")
        var = input("Введите номер варианта: ")
        
    if var == "1":
        with open("data_first.txt", "a", encoding = "utf-8")as file:
            file.write(f"{name}\n{lastname}\n{phonenum}\n{adres}\n\n")
    else:
        with open("data_first.txt", "a", encoding = "utf-8")as file:
            file.write(f"{name}; {lastname}; {phonenum}; {adres}\n\n")
        
def print_data():
    with open("data_first.txt", "r", encoding="utf-8") as data:
        data_first = data.read()
        print(data_first)
    return data_first
        
def search():
    lookfor = input("Кого ищем? ")
    temp_bool = False
    with open("data_first.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
                temp_bool = True
        if temp_bool == False:
            print("Запись не найдена")
            
def load():
    new_phonebook = input("Введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("data_first.txt", "a+", encoding="utf-8") as data_1:
            data_1.write("\n")
            for line in data:
                if line not in data_1:
                    data_1.write(line)
                    
def delete_data():
    line_str = input("Введите запись для удаления: ")
    with open("data_first.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("data_first.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if line_str not in line:
                    data_1.write(line)
                else:
                    print(line)
                    ask = input('Удалить эту строку? (y/n): ')
                    while ask not in ("y", "n"):
                        print("Ввод некорректный")
                        ask = input('Удалить эту строку? (y/n): ')
                    if ask == "n":
                        data_1.write(line)
                    
def change_data():
    line_str = input("Введите запись, которую надо изменить: ")
    with open("data_first.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("data_first.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if line_str not in line:
                    data_1.write(line)
                else:
                    ask = input("Что хотите изменить? (1-Имя, 2-Фамилия, 3-Телефон,4-Адрес): ")
                    while ask not in ("1", "2", "3", "4"):
                        print("Ввод некорректный")
                        ask = input("Что хотите изменить? (1-Имя, 2-Фамилия, 3-Телефон,4-Адрес): ")
                    new_data = input("Введите новые данные: ")
                    line_list = line.split()
                    line_list[int(ask)-1] = new_data  
                    data_1.write("\t".join(line_list)+"\n")
                      