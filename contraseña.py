import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingrsa la longitud de la contraseña"))
password = ""

for i in range(longitud):
    password += random.choice(caracteres)
print(password)
