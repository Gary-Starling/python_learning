#Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы 
#информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

#Кодирование осуществляется следующим образом:
#s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
#на этот символ и количество его повторений в этой позиции строки.

#Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную 
#последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.


s = str(input()) + ' '
s_new = ''
char = ''
len_s = len(s) - 1
i = 0
cnt = 1
#print(len_s)


while i < len_s:
    #print(s_new[i], end ='')
    if s[i] == s[i + 1]: # нашли часть
        cnt += 1
    else:
      char = s[i]
      s_new = s_new + char + str(cnt) 
      cnt = 1
    i += 1

print(s_new)