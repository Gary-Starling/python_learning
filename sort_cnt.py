#Задача на программирование: сортировка подсчётом 

#Первая строка содержит число n
#вторая — n натуральных чисел, не превышающих 10. 
#Выведите упорядоченную по неубыванию последовательность этих чисел.

# put your python code here
a = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0}
n = int(input())
b = input().split()
for i in b:
    a[i] += 1

for key in a:
    if a[key] != 0:
        for i in range(a[key]):
            print(key,end=' ')