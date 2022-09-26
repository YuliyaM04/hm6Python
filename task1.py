# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# СТАРОЕ РЕШЕНИЕ
# n = int(input('Введите число N: '))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print('Произведение чисел числа:', factorial)

n = int(input('Введите число n: '))
fact = lambda a, b:  a * b
f = 1
for i in range(n):
    i+=1
    f = fact(f,i)
    print(f, end=' ')