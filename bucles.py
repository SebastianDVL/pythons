
# numero = 1
# cantidad = 0
# while(numero <= 100):
#     cantidad += numero
#     numero += 13
    
# print(cantidad)


contador = 0
sumatoria = 0

while(contador < 6):
    numero = int(input('Ingrese un numero: '))
    if(numero < 0):  
        sumatoria += 1     
    contador += 1
print(f'La cantidad de numeros negativos fue: {sumatoria}')

