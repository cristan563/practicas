subtotal = float(input("Ingresa el monto de su consumo \n"))
print("que porcentaje dara de proppina")
opcion = int (input("1.- 5% \n" + "2.- 10%\n" + "3.- 15% \n"))

if opcion == 1:
    x = subtotal * .05
    x = x + subtotal
    print("Total : ", x)
elif opcion == 2:
    x = subtotal * .10
    x = x + subtotal
    print("Total : ", x)
elif opcion == 3:
    x = subtotal * .15
    x = x + subtotal
    print("Total : ", x)

