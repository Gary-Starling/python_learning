#Двумерные массивы
#Задача «Максимум»
#Условие
#Найдите индексы первого вхождения максимального элемента.
#Выведите два числа: номер строки и номер столбца, в которых
#стоит наибольший элемент в двумерном массиве. Если таких
#элементов несколько, то выводится тот, у которого меньше
#номер строки, а если номера строк равны то тот, у которого
#меньше номер столбца.
#Программа получает на вход размеры массива n и m,
#затем n строк по m чисел в каждой.

n, m = [int(s) for s in input().split()]
a = []

for i in range(n):
    a.append([int(j) for j in input().split()])

max_i = 0
max_j = 0
maximum = a[0][0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if int(a[i][j]) > maximum:
            max_i = i
            max_j = j
            maximum = int(a[i][j])
    
print(str(max_i) + ' ' + str(max_j))
