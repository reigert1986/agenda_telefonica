
numeros_tel = {
    
}


def opciones():
    try:
        while True:
            eleccion = int(input("ingrese un numero\n"))
            return eleccion
    except Exception as e :
            print(f"el error es = {type(e)} {e}")        
    
def insertar():
    nombre = input("ingrese el nombre del contacto: \n")
    numero = int(input("ingrese el numero del contacto: \n"))
    numeros_tel[nombre] = numero
       
def eliminar():
    try:
        nombre = input("ingrese el nombre a eliminar: \n") 
        del numeros_tel[nombre]
    except Exception as e :
        print(f"el error es = {type(e)} {e}")    

def actualizar():
    print(numeros_tel)
    nombre = input("ingrese el nombre: ")
    numeros_tel[nombre] = int(input("ingrese nuevo numero: \n"))

def busqueda():
    nombre = input("ingrese el nombre: ")
    if nombre in numeros_tel:
        print("el numero esta en la agenda!")
    else:
        print("el numero no esta en la agenda.")    

def mostrar_todos():
    print(numeros_tel)

def main():
    print("opcion 1: insertar ")
    print("opcion 2: eliminar ")
    print("opcion 3: actualizar contacto ")
    print("opcion 4: busqueda ")
    print("opcion 5: mostar contactos ")

    opc = opciones()
    if opc == 1:
     insertar() #insertar
    elif opc == 2:
        eliminar() # eliminar
    elif opc == 3:
        actualizar() # actualizar contacto
    elif opc == 4:
        busqueda() # busqueda
    elif opc == 5:
        mostrar_todos()
    else: 
        print("opcion fuera de rango ")

while True:
    main()
    escape = input("desea terminar? si o no ")
    if escape == "si":
        break

