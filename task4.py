# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# def odd_sum(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# odd_sum(lst)



def odd_sum(a) -> int:
    s = 0
    for i in range(1, len(a), 2):
        s += a[i]
    print(f"Сумма равна: {s}")

a = list(map(int, input("Введите числа через пробел:\n").split()))
odd_sum(a)