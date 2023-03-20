# Sastādīt programmu, kas izvada burtus no `A` līdz `L` tabulas izskatā.

# Definēt 2 dimensionālu sarakstu ar 4 rindām un 3 kolonām, aizpildīt to ar `None` vērtībām. 
# Piemeri: 
# rindas, kolonas = 3, 4 # definējam saraksta lielumu
# saraksts = [[None] * kolonas for i in range(rindas)] # aizpildam ar None vērtībām

# Piešķirt saraksta elementiem vērtības `A`, `B`, ....., `L`.


# Uzdevumi:
# 1) izvadīt sarakstu šādā formātā:
# A B C D
# E F G H
# I  J K L


# 2) izvadīt sarakstu šādā formātā:
# L K J  I
# H G F E
# D C B A

# Pievienot sastādīto programmu *.py un iesniegt.

# Definējam 2-dimensionālu sarakstu ar None vērtībām
rindas, kolonas = 3, 4
saraksts = [[None] * kolonas for i in range(rindas)]

# Piešķiram burtus saraksta elementiem
burts = 'A'
for rinda in range(rindas):
    for kolona in range(kolonas):
        saraksts[rinda][kolona] = burts
        burts = chr(ord(burts) + 1)

# Izvadam sarakstu formātā 1
print("Saraksts formātā 1:")
for rinda in saraksts:
    for kolona in rinda:
        print(kolona, end=" ")
    print()

# Izvadam sarakstu formātā 2
print("Saraksts formātā 2:")
for rinda in saraksts:
    for kolona in reversed(rinda):
        print(kolona, end=" ")
    print()
