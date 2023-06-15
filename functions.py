""" En este programa se harán las funciones que luego serán importadas
al programa principal"""
from os import system
def user_option():
    while True:
        try:
            print("-----ISAPRE VIDA Y SALUD----")
            print("1.Grabar\n2.Buscar")
            userOption = int(input("Ingrese un dígito: "))
            
            if userOption == 1:
                return userOption
            elif userOption == 2:
                return userOption
            elif userOption == 3:
                return userOption
            elif userOption == 4:
                return userOption
            else:
                print("Dígito fuera de las opciones.")
        except ValueError:
            print("Caracter no válido")


def user_input(fichas, message, num=False, rut=False, name=False, chr=False, genre = False): 
    #El argumento message recibe un mensaje personalizado para diferentes input.
    #El segundo argumento permite decidir que tipo de dato debe ingresar el usuario, por defecto es un string.
    while True:
        try:
            if num == False:
                value = input(message)
                if rut == True:
                    #---------------------------------Validación RUT-------------------------------------------
                    if len(value) != 9:
                        print("Rut inválido.")
                        continue
                    #Si el último caracter del rut no se encuentra en la secuencia se imprime que el rut no es válido.
                    if value[-1].upper() not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "K"]: 
                        print("Rut inválido.")
                        continue
                    for i in fichas:
                        if i[0] in fichas:
                            print("El RUT ya tiene una ficha.")
                            break
                    #------------------------------------------------------------------------------------------
                elif name == True:
                    #---------------------------------Validación Nombre/Apellido-------------------------------
                    if len(value) <= 2:
                        print("Nombre demasiado corto.")
                        continue
                    #------------------------------------------------------------------------------------------
                elif chr == True: #Le nombré chr, ya que es solamente 1 caracter.
                    if genre == False:
                        
                        if value.upper() not in ["C", "S", "V"]:
                            print("Estado civíl no válido.")
                            continue
                    
            else:
                value = int(input(message))
            return value
        except ValueError:
            print("Caracter no válido.")

def grabar_ficha(fichas): #El argumento fichas recibe como valor la lista definida en main.py
    system("cls")

    while True:
        rut = user_input("Ingrese RUT: ", rut=True) 
        #Le mando a la función que si es un ingreso tipo rut para hacer su respectiva validación.
        
        
        name = user_input("Ingrese Nombre: ", name=True)
        #Validación Nombre
        if len(name) <= 2:
            print("Nombre demasiado corto.")
            
        
        
        lastName = user_input("Ingrese Apellido Paterno:")
        age = user_input("Ingrese Edad: ", True)
        maritalStat = user_input("Ingrese Estado Civil (C = Casado, S = Soltero, V = Viudo/a): ", chr=True)
        genre = input("Ingrese Género (H = Hombre, M = Mujer): ")
        afiDate = input("Ingrese Fecha Afiliación (dd-mm-aaaa): ")
        
        break
    
            
    ficha = [rut, name, lastName, age, maritalStat, genre, afiDate]
    fichas.append(ficha)


def buscar_ficha(fichas):
    system("cls")
    
    search = user_input("Ingrese RUT: ", rut=True)
    
    for ficha in fichas:
        if ficha[0] == search:
            print(f"""
                Datos Ficha:
                RUT: {ficha[0]}
                Nombre: {ficha[1]}
                Apellido Paterno: {ficha[2]}
                Edad: {ficha[3]}
                Estado Civil: {ficha[4]}
                Género: {ficha[5]}
                Fecha de afiliación: {ficha[6]}""")
    else:
        print("El RUT no posee una ficha.")