# Uzdevumi:
# 1) saskaitīt un izvadīt atbildi cik dotajā tekstā ir burti `a`. Ņemiet vērā ka var būt arī lielie burti `A`.
# 2) cik tekstā ir simboli kopā,
# 3) cik tekstā ir vārdi,
# 4) cik tekstā ir pieturzīmes,
# 5) cik tekstā ir teikumi,
# 6) aizvietojam visus punktus ar izsaukuma zīmi un izvadam iegūto tekstu,
# 7) saskaitam un izvadam cik šajā tekstā vispār ir kādi simboli, piem. a - 7, b - 3, c - 2, ...,
# 8) saskaitam cik tādu ir un izvadam visus tos vārdus, kuros ir vismaz 1 `a` burts.

# izveidojam failu `teksts.txt` un iekopējam tajā patvaļīgu tekstu, saglabājam

# nolasam informāciju no faila `teksts.txt`
f = open("teksts.txt", "r", encoding = "utf8")
a = f.read()
f.close() # aizveram failu

# 1.izvadam visu nolasīto informāciju uzreiz
print(a)

# 2.izvadam nolasīto saturu pa 1 simbolam - dotajā gadījumā katrs simbols jaunā rindā
for i in range(len(a)):
    print(a[i])

# 3.izvadam nolasīto saturu pa 1 simbolam - dotajā gadījumā simboli viens aiz otra
for i in range(len(a)):
    print(a[i], end="")

# uzdevuma risinājums:
# 1.uzd risinajums
 
a_skaits= 0 
print()
for i in range(len(a)):
    if (a[i].lower () ==  "a"):
        a_skaits += 1
print('a vai A burti tekstā bija', a_skaits, "Reizes.")