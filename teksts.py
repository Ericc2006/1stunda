MAPE = "faili/"

mainigais = open("teksts.txt", "r", encoding="utf-8")
print(mainigais.read())

for x in mainigais:
    print(x)

mainigais.close()