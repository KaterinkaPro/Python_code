# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


n = int(input('Введите количество элементов в массиве: '))
list_1 = [int(input()) for item in range(n)]
x = int(input('Введите число, которое нужно проверить: '))
count = 0

for i in range(len(list_1)):
    if x - list_1[i] < x - count and x - list_1[i] > 0:
        count = i
print('Ближайшее число к заданному числу: ', list_1[count])