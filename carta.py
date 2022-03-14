print("Recibir Votos")

opcion = 0
opcion2 = 0
senado = 0
camara = 0
pacto = 0
centro = 0
equipo = 0

while(opcion != 4):
    print("\n1)Senado\n2)Camara\n3)Consulta\n4)Salir Y Mostrar Resultados\n")
    opcion = int(input("Ingrese una opcion del menu: "))

    if opcion == 1:
        senado += int(input("\nIngrese la cantidad de votos al senado: "))
    if opcion == 2:
        camara += int(input("\nIngrese la cantidad de votos a la camara: "))
    if opcion == 3:
        print("\n  Consulta:\n\n  1)Pacto\n  2)Centro\n  3)Equipo\n  4)salir\n")

        while(opcion2 != 4):
            opcion2 = int(input("\ningrese Una Opcion: "))

            if opcion2 == 1:
                pacto += int(input("\nIngrese la cantidad de votos para Pacto: "))
            if opcion2 == 2:
                centro +=int(input("\nIngrese la cantidad de votos para Centro: "))
            if opcion2 == 3:
                equipo += int(input("\nIngrese la cantidad de votos para Equipo: "))


print(f'\nCantidad de votos totales: \n\nSenado: {senado}\nCamara: {camara}\nPacto: {pacto}\nCentro: {centro}\nEquipo: {equipo}\n')


    
    