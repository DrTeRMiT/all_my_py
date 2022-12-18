# 2. Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.
# Примеры:

#  - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# a = int(input('1е число: '))
# b = int(input('2е число: '))
# c = int(input('3е число: '))
# d = int(input('4е число: '))
# e = int(input('5е число: '))

# max = a

# if max < b: max = b
# if max < c: max = c
# if max < d: max = d
# if max < e: max = e
# print (max)


print('введите количество чисел: ')
x = int(input())


def Max(ar):
    max = ar[0]
    for i in range(0, len(ar)):
        if ar[i] > max:
            max = ar[i]
    return max


arr = []

for i in range(x):
    arr.append(int(input(f'Введите число {i+1}: ')))

max = Max(arr)

print(arr)
print(max)
