#Занятие 8. Функции и рекурсия
#Задача «Разворот последовательности»
#Условие
#Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
#При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. Рекурсия вам поможет.

def rec_out():
    out = int(input())
    if out != 0:
        rec_out()
    print(out)
    
rec_out()    