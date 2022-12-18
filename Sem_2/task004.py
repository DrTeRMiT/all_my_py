# Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.
# 10 чисел в диапазоне от 2 до 5

# import random

# n = int(input())
# list = []

# for i in range(n):
#     list.append(random.randint(2, 5))

# print(list)

# max = 0
# for i in range(n):
#     if list.count(list[i]) > max:
#         max = list.count(list[i])

# print(max)

import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(max(count))
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')
