# numeros = []

# cantidad = int(input("Ingrese la cantidad de numeros en el array: "))

# # for i in range(cantidad):
# #     i *= 7
# #     numeros.append(i)



# for i in range(cantidad):
#     i = int(input("ingrese numero: "))
#     numeros.append(i)
# print(numeros)

from ctypes.wintypes import PINT


ciudades = []

for i in range(8):
    ciudad = input("Ingresar Ciudad: ")
    ciudades.append(ciudad)
print(ciudades[::-1])