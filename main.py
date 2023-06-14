import functions

fichas = []
menu = 1

while menu == 1:
    userOption = functions.user_option("1.Grabar\n2.Buscar\n3.Imprimir certificado afiliación\n4.Salir")
        
    if userOption == 1:
        while True:
            fichas.extend(functions.grabar_ficha(fichas))
            print(fichas)
            break
    elif userOption == 2:
        while True:
            functions.buscar_ficha(fichas)
            break
    elif userOption == 3:
        while True:
            functions.impr_certificado(fichas)
            break
    elif userOption == 4:
        while True:
            menu = functions.exit_program(menu)
            break