import os

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.

# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.

# Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar 5bs 
# y si es mayor de 18 años, 10bs.

os.system("clear")

print("¡Bienvenid@s!\n")
edad = int(input("Ingrese la edad: "))

if edad < 4:
    print(f"La Entrada es gratis, Tienes {edad} años")
elif edad >= 4 and edad <= 18:
    print(f"Debe pagar 5bs, Tienes {edad} años")
else:
    print(f"Debe pagar 10bs, Tienes {edad} años")
