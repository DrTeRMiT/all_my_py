# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число: '))
num = 1
print(num, end = " ")
for i in range(1, n):
    num*=-3
    print(num, end = " ")