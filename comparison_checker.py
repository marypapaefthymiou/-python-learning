# Program: Number comparison & even/odd checker

# Ζητάμε δύο αριθμούς από τον χρήστη
a = int(input("Can you give me a number: "))
b = int(input("Can you give me a different number: "))

# Συγκρίνουμε ποιος είναι μεγαλύτερος
if a > b:
    print(f"{a} is bigger than {b}")
elif b > a:
    print(f"{b} is bigger than {a}")
else:
    print(f"{a} and {b} are equal")

# Ζητάμε έναν τρίτο αριθμό
c = int(input("Can you give me another number: "))

# Ελέγχουμε αν είναι άρτιος ή περιττός
if c % 2 == 0:
    print(f"{c} is an Even number")
else:
    print(f"{c} is an Odd number")
