Titulo = input("Introduzca su palabra para generar acronimo ")
proceso = (Titulo.replace('de',' ')).split()
acronimo = ""

for i in proceso:
    acronimo = acronimo + i[0].upper()

print("Resultado: " + str(Titulo) + " es " + acronimo)
