# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

import math

n = int(input("Введите число N: "))

count = 1
i = 0
while count <= n:
    print(f"2^{i} = {count}")
    i += 1
    count = math.pow(2, i)





