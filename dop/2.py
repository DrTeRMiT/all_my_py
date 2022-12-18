# import random
#
# list_num = []
# max = 0
# for i in range(10):
#     a= random.randint(2,5)
#     list_num.append(a)
# print(list_num)
# print(set(list_num))
# for i in set(list_num):
#     if list_num.count(i)>max:
#         max = list_num.count(i)
# print(max)

import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

print(set(array))
d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

max = 0
for i in range(a, (b + 1)):
    if (d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")
