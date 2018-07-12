import random
x = "# KURS MATEMATYKI #"

print("#"*len(x))
print(x)
print("#"*len(x), end="\n\n")
print("\n".join(["1. Dodawanie", "2. Odejmowanie", "3. Mnożenie", "4. Dzielenie", "5. Wyjście"]), end="\n\n")


def fun_1():
    print("Prawidłowy wynik")
    a = str(random.randint(1, 100))
    b = str(random.randint(1, 100))
    return a, b


choice = 0
while choice != 5:
    a = str(random.randint(1, 100))
    b = str(random.randint(1, 100))
    choice = int(input("Wybierz działanie: "))
    if choice == 1:
        d = float(input((a + " + " + b + " = ")))
        while int(a) + int(b) != d:
            print("Błędny wynik")
            d = float(input((a + " + " + b + " = ")))
        else:
            fun_1()
    if choice == 2:
        d = float(input((a + " - " + b + " = ")))
        while int(a) - int(b) != d:
            print("Błędny wynik")
            d = float(input((a + " - " + b + " = ")))
        else:
            fun_1()
    if choice == 3:
        d = float(input((a + " * " + b + " = ")))
        while int(a) * int(b) != d:
            print("Błędny wynik")
            d = float(input((a + " * " + b + " = ")))
        else:
            fun_1()
    if choice == 4:
        print("Zaokrąglij do 3 miejsc po przecinku")
        d = round(float(input((a + " / " + b + " = "))), 3)
        while round((float(a) / float(b)), 3) != d:
            print("Błędny wynik")
            d = float(input((a + " / " + b + " = ")))
        else:
            fun_1()
