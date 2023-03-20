# Klases darbs

# Dota programma:
# ====================================
# // Programma ģenerē 2-dimensiu masīva (4 rindām un 5 kolonām) nejaušus skaitļus
# // un izvada tos tabulas/matricas formā

# program project1;
# var t: array[1..4,1..5] of integer;
#   i,j: integer;
# begin
#   randomize;
#   for i:=1 to 4 do
#       for j:=1 to 5 do
#           t[i,j]:=random(99);

#   for i:=1 to 4 do
#       begin
#       for j:=1 to 5 do
#           write(t[i,j]:3);
#       writeln;
#       end;

# readln;
# end.

import random

r = 4  # rindu skaits
k = 5  # kolonnu skaits

t = [[random.randint(0, 2) for j in range(k)] for i in range(r)]  # nejauši skaitļi no 0 līdz 2

# Izvadam sākotnējo masīvu
print('Sākotnējais masīvs:')
for i in range(r):
    for j in range(k):
        print(t[i][j], end=' ')
    print()

# Veidojam jauno masīvu, aizstājot skaitļus ar burtiem
newt = [['O' if t[i][j] == 0 else '-' if t[i][j] == 1 else 'X' for j in range(k)] for i in range(r)]

# Izvadam jauno masīvu
print('Jaunais masīvs:')
for i in range(r):
    for j in range(k):
        print(newt[i][j], end=' ')
    print()
