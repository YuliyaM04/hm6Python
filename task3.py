# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def comp_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# comp_lst(lst)

from random import randint

number = int(input('Введите размер списка: '))
list = [randint(0, 9) for i in range(number)]
list2 = []

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number -= 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)