# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# СТАРОЕ РЕШЕНИЕ

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# n_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(n_lst) - min(n_lst))

from random import uniform

n = int(input('Введите размер списка: '))
list1 = [round(uniform(0,9),2) for i in range(n)]

min = min(list1, key=lambda i: float(i))
max = max(list1, key=lambda i: float(i))

dif = (max - int(max)) - (min - int(min))

print(list1)
print(round(dif,2))