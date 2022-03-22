#Словари
#Задача «Номер появления слова»
#Условие
#В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
#Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

s = input()
a = s.split()
#print(a)

d = {}

for key in a:
    if key in d:
        d[key] += 1
        print(d[key], end = ' ')
    else:
        d[key] = 0
        print(d[key], end = ' ')