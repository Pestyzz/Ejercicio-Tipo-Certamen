# Funciones del programa
import numpy as np
import os

#Función para validar las opciones que escoja el usuario.
def user_option(message):
    while True:
        try:
            print(message)
            userOption = int(input(""))
            if userOption == 1:
                return userOption
            elif userOption == 2:
                return userOption
            elif userOption == 3:
                return userOption
            elif userOption == 4:
                return userOption
            else:
                print("Su opción no se encuentra dentro de las mostradas.")
        except ValueError:
            print("Opción no válida. Inserte un número con la opción que desea.")
#-----------------------------------------------------------------------------------------
#Función que se llama al seleccionar la opción 1. El usuario debe ingresar los datos solicitados correctamente, de manera que no lo haga será enviado al menú principal.
def grabar_ficha(fichas):
    os.system("cls")
    
    fichas = [] #Se define la lista fichas
    
    while True:
        try:
            #Ingreso RUT
            rut = input(">Ingrese su rut: ").upper()
            #Validación RUT
            if len(rut) != 9: #El largo del rut es un máximo de 9 caracteres.
                print("Rut erróneo. Debe tener máximo 9 caracteres.")
                break
            else:           
                if rut[-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'K']: #El último valor del rut debe de ser uno de estos.
                    print("Rut no válido.")
                    break
            
            #------------------------------------------------------------------------
            #Ingreso Nombre
            name = input(">Ingrese su nombre: ")
            #Validación nombre
            if any(char.isdigit() or not char.isalpha() for char in name): #Se verifica que ningún caracter del nombre sea un número o algún otro caracter.
                print("Su nombre no puede contener números o algún otro caracter inválido.")
                break
            else:
                if len(name) <= 2: #Se verifica que el nombre sea más largo de 2 caracteres para ser válido.
                    print("Nombre muy corto.")
                    break 
            #-------------------------------------------------------------------------
            #Ingreso Apellido
            lastName = input(">Ingrese su apellido: ")
            #Validación apellido
            if any(char.isdigit() or not char.isalpha() for char in lastName): #Lo mismo que en name
                print("Su apellido no puede contener números.")
                break
            if len(lastName) <= 2: #Lo mismo que en name
                print("Apellido muy corto.")
                break
            #-------------------------------------------------------------------------
            #Ingreso Edad
            age = int(input(">Ingrese su edad: "))
            #Validación Edad
            if age < 18: #Se verifica que sea mayor de edad.
                print("Debe ser mayor de edad.")
                break
            elif age <= 0: #La edad debe ser mayor a cero para ser una edad válida.
                print("Edad inválida.")
            else:
                age = f"{age} años"
            #--------------------------------------------------------------------------
            #Ingresar Estado Civil
            maritalStatus = input(">Ingrese su estado civil (C = Casado, S = Soltero, V = Viudo): ")
            #Validación Estado Civil
            if len(maritalStatus) < 2: #Se verifica que el largo de lo que ingrese el usuario deba de ser de 1 letra.
                pass
            else:
                print("Debe escribir solamente una letra.")
            if maritalStatus != "C" and maritalStatus != "S" and maritalStatus != "V": #El valor debe de ser una de las tres letras.
                print("Estado civil inválido.")
                break
            else:
                if maritalStatus == "C":
                    maritalStatus = "Casado"
                elif maritalStatus == "S":
                    maritalStatus = "Soltero"
                elif maritalStatus == "V":
                    maritalStatus = "Viudo"
            #----------------------------------------------------------------------------
            #Ingreso Género
            genre = input(">Ingrese su género (H = Hombre, M = Mujer): ")
            #Validación Género
            if len(genre) < 2:
                pass
            else:
                print("Debe escribir solamente una letra.")
                break
            if genre != "H" and genre != "M":
                print("Género inválido.")
                break
            else:
                if genre == "H":
                   genre = "Hombre"
                elif genre == "M":
                    genre = "Mujer"
            #-----------------------------------------------------------------------------
            #Ingreso Datos Fecha Afiliación y Validaciones
            day = int(input("Ingrese el DÍA de su fecha de afiliación: "))
            if day > 31 or day <= 0:
                print("Día inválido")
                break
            
            month = int(input("Ingrese el MES de su fecha de afiliación: "))
            if month > 12 or month <= 0:
                print("Mes inválido.")
                break
                
            year = int(input("Ingrese el AÑO de su fecha de afiliación: "))
            if year > 2023 or year <= 2013:
                print("Año fuera del rango o inválido.")
                break
            
            afiliateDate = [day, month, year] #Los datos de la fecha se almacenan en una lista
            
            afiliateDate = '-'.join(map(str, afiliateDate)) #Le doy formato a la fecha uniendo los valores de la lista con "-".join(), transformo los int a str con map((str, afiliateDate))
            #-----------------------------------------------------------------------------
            ficha = [rut, name, lastName, age, maritalStatus, genre, afiliateDate] #Se almacenan todos los datos en un array.
            #fichaString = " ".join(ficha) 
            fichas.append(ficha) #Se agrega una nueva ficha a la lista fichas
            
            """ certificado = " ".join(ficha)
            print(certificado)
             """
            return fichas
          
        except ValueError:
            print("Caracter inválido.")
            break
        
def execute_program(fichas):
    menu = 1
    fichas = []
    while menu == 1:
        userOption = user_option("1.Grabar\n2.Buscar\n3.Imprimir certificado afiliación\n4.Salir")
        
        if userOption == 1:
            while True:
                fichas.extend(grabar_ficha(fichas))
                print(fichas)
                break