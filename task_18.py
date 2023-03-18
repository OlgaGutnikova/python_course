# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
array_A = []
n = int (input('Введите количество элементов массива: '))
x = int(input('Введите число Х: '))
for i in range(n):
    array_A.append(randint(1, 10))
ch = array_A[0]
difference = abs(abs(array_A[0]) - x)
for i in range(n):
    if abs(abs(array_A[i]) - x) < difference and abs(abs(array_A[i]) - x) != 0:
        ch = array_A[i]
        difference = abs(abs(array_A[i]) - x)
print(array_A)
print(ch)
