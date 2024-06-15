import random

Caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud = int(input("Introduzca el numero de digitos de su contraseña"))

Contrasena = ""
for i in range(Longitud):
    Contrasena += random.choice(Caracteres)
print(Contrasena)