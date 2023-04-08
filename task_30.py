# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progess(number, difference,count):
    list=[]
    for i in range(1,count+1):
        list.append(number + (i-1)*difference)
    return list

number = int(input('Введите первый элемент: '))
diff = int(input('Введите разность (шаг): '))
count = int(input('Введите количество элементов: '))
print(*progess(number, diff, count))