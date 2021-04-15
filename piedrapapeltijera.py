import random
pc = random.randint(1,3)
opc = input("Introduce piedra papel o tijera \n")
if opc=="papel" and pc==1:
    print("Ganaste papel vence a piedra")

elif opc=="piedra" and pc==3:
    print("Ganaste piedra vence a tijeras")

elif opc=="tijeras" and pc==2:
    print("Ganaste tijeras vence a papel")

else:
    print("Perdiste, Intentalo denuevo")
