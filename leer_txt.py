def menu():
    while True:
        opcion = input("1.- Leer un archivo\n2.- Salir\nelige una opcion: ")
        if opcion == "1":
            lectura_de_archivo()
        elif opcion == "2":
            break
        else:
            print("Ingrese una opción valida")

def lectura_de_archivo():
    nombre_de_archivo = input("Ingrese el nombre del archivo que desea leer: ")

    with open(nombre_de_archivo, "r") as archivo:
            texto = archivo.read()
            uno_letras = len(texto)
            uno_espacios = texto.count(" ")
            total_de_letras = uno_letras - uno_espacios
    with open("archivo.txt", "w") as archivo_salida:
            archivo_salida.write(f"La cantidad de letras del archivo que ingresaste es {total_de_letras} y la cantidad de espacios que contiene es {uno_espacios}\n")
    print(f"La cantidad de letras del archivo que ingresaste es {total_de_letras} y la cantidad de espacios que contiene es {uno_espacios}")

menu()