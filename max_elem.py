#Цикл while
#Задача «Количество элементов, равных максимуму»
#Условие
#Последовательность состоит из натуральных чисел и завершается числом 0.
#Определите, сколько элементов этой последовательности равны ее наибольшему
# элементу.

x = max = pr_max = int(input())
cnt = 1
while x:
    pr_max = max
    x = int(input())
    if x >= max:
        max = x
        if pr_max == max:
            cnt += 1
        else:
            cnt = 1
        

print(cnt)
