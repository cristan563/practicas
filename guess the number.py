import random

num = random.randint(1, 10)
t=0
print("Tienes 5 intentos \n")


while t < 5:
    t = t + 1
    x = input("Adivina el numero")
    if int(x) < num:
        print("demasiado bajo")
    if int(x) > num:
        print("demasiado alto")
    elif int(x) == num:
        print("le atinaste")
        break
