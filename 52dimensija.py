# Izveidot 2 dimensiju sarakstu ar X rindām un X kolonnām, kur X ievada lietotājs. 
# Jāņem vērā, ka X nevar būt mazāks par 2 un lielāks par 20. 
# Aizpildīt ar nejaušiem skaitļiem no 0 līdz 9 (ieskaitot). 
# Izvadīt sarakstu tabulas izskatā elementus atdalot ar atstarpi (bez komatiem).

# Izvadīt pirmās kolonas visus elementus vienā rindā atdalot ar atstarpi (bez komata).
# Izvadīt tabulas abu 'diagonāļu' elementu vērtības un to summu!
# Iesniegt risinājumu kā *.py failu.

import random

x = 0
while x < 2 or x > 20:
    x = int(input("ievada x vērtību no 2 līdz 20 = "))
    if x < 2:
        print ("nepareiz ievadīts x jābūt lielākam par 1 un mazākam par 20")
    if x > 20:
        print ("nepareiz ievadīts x jābūt lielākam par 1 un mazākam par 20")

saraksts = [[None] * x for i in range (x)]
print(saraksts)

for i in range(x):
    for j in range(x):
        saraksts[i][j] = random.randint(0,9)

print (saraksts)

for m in saraksts:
    for u in m:
        print (u, end =" ")
    print()

sum = 0

for i in range(x):
    sum = sum + saraksts[i][i]

