# Program: Μάντεψε τον αριθμό, έχεις 7 προσπάθειες

import random

secret = random.randint(1, 100)  # τυχαίος αριθμός
x = 0  # μετρητής προσπαθειών
max_x = 7
guess = 0

print("Μπορείς να μαντέψεις τον αριθμό; Έχεις 7 προσπάθειες!")

while guess != secret and x < max_x:
    guess = int(input("Δώσε έναν αριθμό από 1 έως 100: "))
    x += 1
    
    if guess < secret:
        print(f"{guess} είναι μικρότερος από τον μυστικό. Προσπάθησε ξανά!")
    elif guess > secret:
        print(f"{guess} είναι μεγαλύτερος από τον μυστικό. Προσπάθησε ξανά!")
    else:
        print(f"Μπράβο! Το βρήκες σε {x} προσπάθειες!")

if guess != secret:
    print(f"Έχασες! Ο αριθμός ήταν {secret}.")
