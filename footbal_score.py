# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.


n = int(input())
d = {}

for i in range(n):
    com1, res1, com2, res2 = input().split(";")
    if com1 not in d:
        d[com1] = {"all": 0, "win": 0, "eq": 0, "lose": 0, "score": 0}
    if com2 not in d:
        d[com2] = {"all": 0, "win": 0, "eq": 0, "lose": 0, "score": 0}

    # all games
    d[com1]["all"] += 1
    d[com2]["all"] += 1

    if int(res1) > int(res2):
        d[com1]["win"] += 1
        d[com1]["score"] += 3
        d[com2]["lose"] += 1
    elif int(res1) < int(res2):
        d[com2]["win"] += 1
        d[com2]["score"] += 3
        d[com1]["lose"] += 1
    elif int(res1) == int(res2):
        d[com1]["score"] += 1
        d[com2]["score"] += 1
        d[com1]["eq"] += 1
        d[com2]["eq"] += 1

for key in d:
    print(
        key+":"+str(d[key]["all"]),
        d[key]["win"],
        d[key]["eq"],
        d[key]["lose"],
        d[key]["score"],
    )
