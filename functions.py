""" En este programa se harán las funciones que luego serán importadas
al programa principal"""

def user_option():
    while True:
        try:
            print("1. Grabar\n2.Buscar")
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
            
def grabar_ficha(fichas):
    rut = input("Ingrese RUT: ")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido Paterno: ")
    edad = int(input("Ingrese Edad: "))
    estadoCivil = input("Ingrese Estado Civil (C = Casado, S = Soltero, V = Viudo/a): ")
    genero = input("Ingrese Género (H = Hombre, M = Mujer): ")
    fechaAfi = input("Ingrese Fecha Afiliación (dd-mm-aaaa): ")
    
    ficha = [rut, nombre, apellido, edad, estadoCivil, genero, fechaAfi]
    fichas.append(ficha)

def buscar_ficha(fichas):
    

    