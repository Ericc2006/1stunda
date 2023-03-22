# Loterijas uzdevums (izmantojot list/sarakstu)

# Sastādīt programmu, kas realizē skaitļu loteriju 5 no 20.
# Jāņem vērā, ka 5 skaitļus no 20 ģenerē programma.
# Skaitļi a) var atkārtoties, b) nedrīkst atkārtoties! Saglabāt skaitļus masīvā.
# Skaitļus sākumā nevajag izvadīt uz ekrāna. 
# Lietotājam jāpiedāvā ievadīt 5 minamie skaitļi. 
# Programma pārbauda vai ir uzminets vismaz 1 skaitlis un ja uzminēti 1 vai vairāki, tad izvada cik un kuri skaitļi ir uzminēti. 
# Programma izvada 5 skaitļus, ko sākotnēji ģenerēja dators.
# Programmu radoši papildināt ar punktu un/vai iespējamo laimestu aprēķināšanu un izvadīt tos. 
# Programma dod iespēju veikt minēšanu vēlreiz ar citiem ģenerētajiem skaitļiem.

import random

# ģenerē 5 nejaušus skaitļus no 1 līdz 20, bez atkārtojumiem
def generate_numbers():
    skaitlu_kopa = list(range(1, 21))
    random.shuffle(skaitlu_kopa)
    return skaitlu_kopa[:5]

# salīdzina minējumus ar ģenerētajiem skaitļiem, atgriež uzminēto skaitļu skaitu un pašus skaitļus
def compare_numbers(minetie_skaitli, uzminetie_skaitli):
    uzmineti = list(set(minetie_skaitli) & set(uzminetie_skaitli))
    return len(uzmineti), uzmineti

# izvada iespējamo laimestu summu atkarībā no uzminēto skaitļu skaita
def print_winnings(uzmineti_skaitli):
    uzminetie_skaitli_skaits = len(uzmineti_skaitli)
    if uzminetie_skaitli_skaits == 5:
        print("Apsveicam, jūs uzvarējāt 10 000 eiro!")
    elif uzminetie_skaitli_skaits == 4:
        print("Apsveicam, jūs uzvarējāt 1000 eiro!")
    elif uzminetie_skaitli_skaits == 3:
        print("Jūs uzvarējāt 50 eiro!")
    elif uzminetie_skaitli_skaits == 2:
        print("Jūs uzvarējāt 10 eiro!")
    elif uzminetie_skaitli_skaits == 1:
        print("Jūs uzvarējāt 5 eiro!")
    else:
        print("Diemžēl šoreiz jums neizdevās uzvarēt.")

# sākam programmu
print("Sveiki, šī ir skaitļu loterija 5 no 20!")
print("Lai sāktu, lūdzu, ievadiet 5 skaitļus no 1 līdz 20, atdalot tos ar komatu:")
minetie_skaitli = input().split(",")
minetie_skaitli = [int(skaitlis) for skaitlis in minetie_skaitli]

if len(minetie_skaitli) != 5:
    print("Nepareizs ievades formāts. Lūdzu, ievadiet 5 skaitļus, atdalot tos ar komatu.")
else:
    uzminetie_skaitli = generate_numbers()
    print("Ģenerētie skaitļi:", uzminetie_skaitli)
    uzminetie_skaitli_skaits, uzminetie_skaitli = compare_numbers(minetie_skaitli, uzminetie_skaitli)
    print("Jūs uzminējāt " + str(skaitluSakritiba) + " skaitļus! Skaitļi, kuri sakrita: " + str(atbilde))

