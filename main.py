# # logica con python
# edad = int(input("Ingrese su edad: "))
# msg = "Eres Mayor de edad" if edad > 17 else "Eres Menos de Edad"
# print(f"Tienes {edad} años, {msg}")

from multiprocessing.connection import wait
from tkinter import W


mes = input("Ingrese un mes: ").lower().replace(' ','')

if(mes == "enero" or mes =="febrero" or mes == "marzo"):
    print("La estacion del año es Invierno")
elif(mes == "abril" or mes ==  "mayo" or mes == "junio"):
    print("La estacion del año es Verano")
elif(mes == "julio" or mes == "agosto" or mes == "septiembre"):
    print("La estacion del año es Otoño")
elif(mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
    print("La estacion del año es Primavera")
else:
    print(f"{mes} No es un mes valido")

