
#Шахматная ладья ходит по горизонтали или вертикали. 
#Даны две различные клетки шахматной доски, 
#определите, может ли ладья попасть с первой клетки на вторую одним ходом.
#Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер 
#столбца и номер строки сначала для первой клетки, потом для второй клетки.
#Программа должна вывести YES, если из первойклетки ходом ладьи можно
#попасть во вторую или NO в противном случае.
#Ввод данных
st1 = int(input())
str1 = int(input())
st2 = int(input())
str2 = int(input())

#Если мы 
if st1 == st2 or str1 == str2:
    print('YES')
else:
    print('NO')