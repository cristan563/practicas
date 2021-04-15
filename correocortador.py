correo = input("ingrese su correo electronico \n").strip("")
arroba = correo.index('@')
usuario = correo[:arroba]
dominio = correo[arroba+1:]
print("Correo: " + correo)
print("Usuario: " + usuario)
print("Dominio: " + dominio)


