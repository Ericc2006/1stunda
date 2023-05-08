# Šī ir spēle, kurā jāuzmin skaitlis no 1 līdz 10.
# Spēlētājam ir 3 mēģinājumi.

import random

number = random.randint(1, 10)
attempts = 3

print("Sveiki! Šajā spēlē jums ir jāuzmin skaitlis no 1 līdz 10. Jums ir 3 mēģinājumi.")

while attempts > 0:
    guess = int(input("Uzminiet skaitli: "))
    attempts -= 1

    if guess == number:
        print("Apsveicam! Jūs uzminējāt skaitli.")
        break
    elif guess > number:
        print("Skaitlis ir mazāks.")
    else:
        print("Skaitlis ir lielāks.")

    if attempts == 0:
        print("Diemžēl jums beidzās mēģinājumi. Skaitlis bija", number)
