import msvcrt

'''
crear un fichero de texto txt
con diferentes campos:
id nombre edad marca modelo
10 personas
necesitamos un menu por pantalla
añadir registros
pedir nombre edad y demas
comprobar si es entero
lo añadimos al dinal open a
segunda opcion del menu es mostrar
por nombre, mostrar mayores de edad
'''
# Funcion para mostrar el fichero entero
fich="C:/Users/christian.campos/Desktop/scripts de python/Busqueda_coches/coches.txt"

def op1():

    try:
        fichero = open(fich, "r")

        for linea in fichero:
            palabras = linea.split()
            print(palabras)


        fichero.close()

    except:
        print("No ha funcionado")

    print()

# Funcion para buscar los nombres y enseñar las cadenas
def op2_1():
    cadena = "x"
    cadena = input("busca un nombre:")
    print("Las entradas que contienen el nombre",cadena,"son: ")
    print()

    try:
        fichero = open(fich, "r")
        
        # solo comprueba el nombre
        for linea in fichero:
            palabras = linea.split()
            palabras = str(palabras[1])

            if cadena.lower() == palabras.lower():
                #print("los coches de ",cadena," son: ", linea)
                print(linea)

        fichero.close()

    except:
        print("No ha funcionado")
    print('''
            ''')
    
# Funcion para filtrar por edades menor, y mayor
def op2_2():

    cadena = "x"
    cadena = input("Indique un rango de edades separada por espacios o una edad única:   ")
    try:
        cadena=cadena.split()
        min=cadena[0]
        max=cadena[1]
    except:
        #si solo detecta un numero
        max=min

    #si no se introduce un numero en algun sitio
    if not min.isdigit():
        print("faltan numeros")
        op2_2()
    if not max.isdigit():
        print("faltan numeros")
        op2_2()
    
    # Control de errores si la introducen a la inversa 
    if (min>max):
        temporal = min
        min = max
        max = temporal
    

    try:
        fichero = open(fich, "r")

        for linea in fichero:
            palabras = linea.split()
            edad=palabras[2]

            if edad<=max and edad>=min:
                print(linea)

        fichero.close()
    except:
        print("No ha funcionado")

# opcion 3 para añadir un registro
def op3():
    print("Se va a añadir un registro...")
    id = input("Introduce el ID: ")
    nombre = input("Introduce el nombre: ")
    edad = input("Introduce la edad del usuario: ")
    marca = input("Introduce la marca del coche: ")
    modelo = input("Introduce el modelo del coche: ")

    registro = f"\n{id} {nombre} {edad} {marca} {modelo}"

    with open(fich, "a") as archivo:
        archivo.write(registro)

# Funcion para obtener la tecla pulsada y no detectar mas letras
def getKey():
    return msvcrt.getch().decode()

############################################## MENÚ ########################################################
def menu():

    while True:
        print("selecciona una opcion: ")
        print("1 - Busqueda registros")
        print("2 - Buscar por Nombre/edades")
        print("3 - añadir registro")
        print("x - salir")

        x = getKey()

        if x == "1":
            op1()
        elif x == "2":
            ######################### MENÚ ANIDADO #########################
            while True:
                print ("elija una opcion:")
                print ("1 - para buscar un nombre")
                print ("2 - para buscar por edades")
                print ("x - atras")
                z = getKey()
                if z == "1":
                    op2_1()
                elif z == "2":
                    op2_2()
                elif z == "x":
                    break
                else:
                    print("pulse una tecla correcta")
            
        elif x == "3":
            op3()
        elif x == "x":
            break
        else:
            print ("")
            print ("No has pulsado nada válido")
            print ("")

# Llamo al menu, y desde el se llaman a todas las funciones
menu()