# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
def summa(a, b):
    if b == 0:
        return a
    sum = 1 + summa(a, b-1)
    return (sum)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(summa(a, b))
