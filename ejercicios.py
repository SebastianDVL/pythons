#Punto1
# numero = int(input("Ingrese un numero: "))
# resultado = "SI es Multiplo de 5" if numero % 5 == 0 else "NO es multiplo de 5"
# print(resultado)

#Punto2
# numero = int(input("Ingrese un numero: "))
# resultado = "SI es Multiplo de 3" if numero % 3 == 0 else "NO es multiplo de 3"
# print(resultado)

# #Punto3
# numero1 = int(input("Ingrese un numero: "))
# numero2 = int(input("Ingrese otro numero: "))
# resultado =  f"{numero1} es mayor" if numero1 > numero2 else f"{numero2} es mayor"
# print(resultado)

#Punto4
# cantidadJuan = int(input("Ingrese la cantidad de dinero de Juan: $"))
# cantidadCamila = int(cantidadJuan / 2)
# cantidadRicardo = int((cantidadJuan + cantidadCamila) / 2)
# print(f"Juan: ${cantidadJuan}\nCamila: ${cantidadCamila}\nRicardo: ${cantidadRicardo}")

#punto5
numeroVentas = int(input("Ingrese el numero de ventas realizadas: "))
comision = numeroVentas * 150000
salario = 350000 + comision - ((350000  + comision) * 0.05) 
print(f"${salario}")