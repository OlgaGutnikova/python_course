# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
s = int(input('Введите общее число журавликов: '))
if s%3 == 0:
    k = int((s/3)*2)
    ps = int((s - k)/2)
    print(f'Катя сделала {k} шт., Петя и Сережа по {ps} шт.')
else:
    print('Заданное количество не делится на три части')