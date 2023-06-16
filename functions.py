""" En este programa se harán las funciones que luego serán importadas
al programa principal"""
from os import system
def user_option():
    while True:
        try:
            print("-----ISAPRE VIDA Y SALUD-----")
            print("1.Grabar\n2.Buscar\n3.Imprimir Certificado\n4.Salir")
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


def user_input(message, fichas=None, search=False, num=False, rut=False, name=False, chr=False, genre=False, date=False): 
    """ El argumento message recibe un mensaje personalizado para diferentes input.
    El segundo argumento se encarga de definir fichas como None, para que no sea obligatorio poner un argumento al llamar a la función.
    Los demás argumentos son para indicar el tipo de dato que se va a ingresar para poder validar ese dato en específico.
    El argumento search es únicamente para en la validación del rut omitir el paso de validar
    si el rut tiene ficha, ya que si no se hace eso no se puede buscar una ficha."""
    while True:
        try:
            if num == False:
                value = input(message)
                if rut == True:
                    value = value.upper()
                    #---------------------------------Validación RUT-------------------------------------------
                    if len(value) != 9:
                        print("Rut inválido.")
                        continue
                    #Si el último caracter del rut no se encuentra en la secuencia se imprime que el rut no es válido.
                    if value[-1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "K"]: 
                        print("Rut inválido.")
                        continue
                    #Se verifica que el rut no tenga una ficha ya creada
                    if search == False:
                        for ficha in fichas:
                            if ficha[0] == value:
                                print("El RUT ya tiene una ficha.")
                                return False
                                #Si hay una ficha existente con ese rut, se devuelve False
                    #------------------------------------------------------------------------------------------
                elif name == True:
                    value = value.capitalize()
                    #---------------------------------Validación Nombre/Apellido-------------------------------
                    for char in value:
                        if char.isdigit():
                            raise ValueError #Si se encuentra algún número en el nombre se lanza un error.
                    if len(value) <= 2:
                        print("Demasiado corto.")
                        continue
                    #------------------------------------------------------------------------------------------
                elif chr == True: #Le nombré chr, ya que es solamente 1 caracter.
                    value = value.upper()
                    if genre == False:
                        if value.isdigit():
                            raise ValueError #Si
                        #Si el caracter no se encuentra en la secuencia no es válido.
                        if value not in ["C", "S", "V"]:
                            print("Estado civíl no válido.")
                            continue
                        else:
                            if value == "C":
                                value = "Casado"
                            if value == "S":
                                value = "Casado"
                            if value == "V":
                                value = "Casado"
                    else:
                        if value.isdigit():
                            raise ValueError
                        #Si el caracter no se encuentra en la secuencia no es válido.
                        if value not in ["H", "M"]:
                            print("Género no válido.")
                            continue
                        else:
                            if value == "H":
                                value = "Hombre"
                            if value == "M":
                                value = "Mujer"
                elif date == True:
                    if len(value) != 10:
                        print("Fecha no válida.")
                        continue
                    #Para hacerlo más simple solamente se va a validar el largo de la fecha.
                    """ Se podría hacer que el usuario ingrese 3 datos
                    día, mes, y año, luego se validaría cada uno para que sea válido,
                    se transformarían a string guardando en una variable los 3 datos con
                    f"{day}-{month}-{year}", y de paso se le daría el formato que es
                    dd-mm-aaaa.
                    """
            else:
                value = int(input(message))
                #---------------------------------Validación Nombre/Apellido-------------------------------
                if value < 18:
                    print("Debe ser mayor de edad.")
                    continue
                else:
                    value = f"{value} años" #Si la edad es correcta, se devuelve en un string
                #------------------------------------------------------------------------------------------
                
            return value
        
        except ValueError:
            print("Caracter no válido.")

def grabar_ficha(fichas): #El argumento fichas recibe como valor la lista definida en main.py
    system("cls")
    while True:
        rut = user_input("Ingrese RUT: ", fichas, rut=True)
        if rut == False: #Si se devuelve False, se regresa al menú principal.
            return
        #Le mando a la función que si es un ingreso tipo rut para hacer su respectiva validación en esa función.
        name = user_input("Ingrese Nombre: ", name=True)
        lastName = user_input("Ingrese Apellido Paterno: ", name=True)
        age = user_input("Ingrese Edad: ", num=True)
        maritalStat = user_input("Ingrese Estado Civil (C = Casado, S = Soltero, V = Viudo): ", chr=True)
        genre = user_input("Ingrese Género (H = Hombre, M = Mujer): ", genre=True, chr=True)
        afiDate = user_input("Ingrese Fecha Afiliación (dd-mm-aaaa): ", date=True)
        break
        
    #maritalStat = Estado Civíl
    
    #Los datos son añadidos a la lista, y esa ficha es añadida a la lista fichas.        
    ficha = [rut, name, lastName, age, maritalStat, genre, afiDate]
    fichas.append(ficha)


def buscar_ficha(fichas):
    system("cls")
    
    search = user_input("Ingrese RUT: ", search=True,rut=True)
    
    for ficha in fichas:
        if ficha[0] == search:
            print(
f"""
Datos Ficha:
RUT: {ficha[0]}
Nombre: {ficha[1]}
Apellido Paterno: {ficha[2]}
Edad: {ficha[3]}
Estado Civil: {ficha[4]}
Género: {ficha[5]}
Fecha de afiliación: {ficha[6]}
""")
            break
                
    else:
        print("El RUT no posee una ficha.")
        
        
def impr_certifi(fichas):
    search = user_input("Ingrese RUT: ", search=True,rut=True)
    
    for ficha in fichas:
        if ficha[0] == search:
            print(
f"""
CERTICADO AFILIACION ISAPRE VIDA Y SALUD

{ficha[1]} {ficha[2]}, RUT {ficha[0]}, cuya edad es {ficha[3]}, sexo {ficha[5]}, estado civil {ficha[4]}, afiliado en esta institución desde el
{ficha[6]}.

Se otorga este certificado de afiliación para los fines que estime conveniente.

Sin otro particular.
""")
            break    
    else:
        print("El RUT no posee una ficha.")

def salir(menu):
    print("Saliendo...\nBastián Ñiripil\nversión 1.2")
    menu = 0
    return menu