""" PROGRAMA PRINCIPAL
En este archivo main.py las funciones del archivo functions.py serán importadas
para utilizarlas."""
import functions as func

menu = 1
fichas = []

while menu == 1:
    userOption = func.user_option()
    
    match userOption:
        case 1:
            func.grabar_ficha(fichas) #Le doy la lista para que la pueda utilizar en la función
            print(fichas)
        case 2:
            func.buscar_ficha(fichas)
        case 3:
            func.impr_certifi(fichas)
        case 4:
            menu = func.salir(menu)