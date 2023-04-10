from logger import *

def interface():
    print('''1 - записать данные, 
     2 - поиск записи,
     3 - вывод на экран,
     4 - импорт в файл,
     5 - удаление записи,
     6 - изменить запись''')
    var = input('Введите номер варианта: ')
    while var not in ("1", "2", "3", "4", "5", "6"):
        print("Вваринт не верный")
        var = input("Введите номер варианта: ")
        
    if var == "1":
        input_data()
    elif var =="2":
        search()
    elif var =="3":
        print_data()
    elif var =="4":
        load()
    elif var =="5":
        delete_data()
    elif var =="6":
        change_data()