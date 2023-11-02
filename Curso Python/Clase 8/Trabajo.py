with open("resultados-del-test.csv", "r") as fil:
    i = 0
    for line in fil.readlines():
        i += 1
        print(line)
        if i == 10:
            break
import pandas
datos = pandas.read_csv("resultados-del-test.csv")
pass
