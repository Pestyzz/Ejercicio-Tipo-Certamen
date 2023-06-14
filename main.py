import functions
import os
os.system("cls")
menu = 1

fichas = []

while menu == 1:
    userOption = functions.user_option("1.Grabar\n2.Buscar\n3.Imprimir certificado afiliación\n4.Salir")
    
    if userOption == 1:
        while True:
            fichas.extend(functions.grabar_ficha(fichas)) #Cada vez que se ingresa una nueva ficha, se extiende el espacio de la lista y se agrega.
            print(fichas)
            break
    elif userOption == 2:
        while True:
            functions.buscar_ficha(fichas)
            break
    elif userOption == 3:
        while True:
            certified = functions.impr_ficha(fichas)
            break