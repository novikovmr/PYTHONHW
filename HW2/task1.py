# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами
# элементы множеств.
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
#
# 6 12

def input_list(count, number_of_list):
    current_list = []
    for i in range(count):
        new_el = int(input(f"Введите {i+1} элемент списка №{number_of_list} : "))
        current_list.append(new_el)
    return current_list


count1 = int(input("Введите кол-во элементов 1-го списка: "))
count2 = int(input("Введите кол-во элементов 2-го списка: "))

a = input_list(count1, 1)
b = input_list(count2, 2)

if set(a).isdisjoint(set(b)):
    print("У множеств нет одинаковых чисел")
else:
    c = set(a).intersection(set(b))

print(sorted(c))