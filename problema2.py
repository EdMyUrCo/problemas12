import os

# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura que sea el número introducido.

os.system("clear")

cant = int(input("Ingrese la altura: "))

simbolo = "*"

for i in range(cant):
    print(simbolo * i)