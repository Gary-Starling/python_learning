#Условие
#Дана строка, состоящая ровно из двух слов, разделенных пробелом.
#Переставьте эти слова местами. Результат запишите в строку и выведите
#получившуюся строку.
#При решении этой задачи не стоит пользоваться циклами и инструкцией if.


s = str(input())

n = s.find(' ')
print(s[n+1::1] + ' ' + s[0:n:1])

