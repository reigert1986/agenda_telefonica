
numeros_tel = {
    
}


def opciones():
    flag = True
    
    try:
        while flag:
            eleccion = int(input("ingrese un numero\n"))
            if type(eleccion) == int:
              flag = False
              print(eleccion)
            return eleccion
    except Exception as e :
            print(f"el error es = {type(e)}")

opciones()            
    
def insertar():
    nombre = input("ingrese el nombre del contacto: \n")
    numero = int(input("ingrese el numero del contacto: \n"))
    numeros_tel[nombre] = numero
       
def eliminar():
    nombre = input("ingrese el nombre a eliminar: \n") 
    del numeros_tel[nombre]

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

def main():
    print("opcion 1: insertar")
    print("opcion 2: eliminar")
    print("opcion 3: actualizar contacto")
    print("opcion 4: busqueda")
    

    opc = opciones()
    if opc == 1:
     insertar() #insertar
    elif opc == 2:
        eliminar() # eliminar
    elif opc == 3:
        actualizar() # actualizar contacto
    elif opc == 4:
        busqueda() # busqueda
  
    else: 
        print("opcion fuera de rango")

while False:
    main()
    escape = input("desea terminar? si o no")
    if escape == "si":
        break

