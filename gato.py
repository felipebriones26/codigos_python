import random
import os
print("¡Bienvenido al juego del gato!")
print("¿Deseas jugar con alguien más o contra la computadora?: ")

def menu():
    while True:
        respuesta = input("""1.- Dos jugadores \n2.- Computadora \n3.- Salir \nIngresa tu opcion: """)
        
        if respuesta == "1":
            print("Elegiste jugar contra otro jugador")
            return "1"
            break
        elif respuesta == "2":
            print("Elegiste jugar contra la computadora")
            return "2"
            break
        elif respuesta == "3":
            print("Elegiste salir del programa, gracias por utilizarlo")
            return "3"
            break
        else:
          print("ingrese una opcion valida")



jugador1= "X"

jugador2= "O"

Computadora= "O"



def reiniciar_tablero():
    global tab
    tab = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]

    


def imprimir_tablero(tab):
    
    print(tab[0] + " | " + tab[1] + " | " + tab[2])
    print("----------")
    print(tab[3] + " | " + tab[4] + " | " + tab[5])
    print("----------")
    print(tab[6] + " | " + tab[7] + " | " + tab[8])
    
def limpiar_terminal():
        os.system('cls')

def eleccion_del_jugador1(tab):
    while True:    
        eleccion = int(input("¡Jugador 1!, tu eres la X, Elige una casilla por su numero: "))
        if eleccion >= 1 and eleccion <= 9 and tab[eleccion-1] != "X" and tab[eleccion-1] != "O":
            tab[eleccion-1] = jugador1
            break
        else:
            print("Casi pero no, intente con otro numero mi rey")
            imprimir_tablero(tab)

def eleccion_del_jugador2(tab):
    while True:    
        eleccion = int(input("¡Jugador 2!, tu eres la O, Elige una casilla por su numero: "))
        
        if eleccion >= 1 and eleccion <= 9 and tab[eleccion-1] != "X" and tab[eleccion-1] != "O":
            tab[eleccion-1] = jugador2
            break
        else:
            print("Casi pero no, intente con otro numero mi rey")
            imprimir_tablero(tab)   

def eleccion_de_computadora(tab):
    print("Eleccion de la computadora")
    
    while True:
        eleccion = random.randint(1, 9)
        if tab[eleccion-1] != "X" and tab[eleccion-1] != "O":
            tab[eleccion-1] = Computadora
            break
    return  eleccion

def verificar_ganador(tab):
    ganadores = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in ganadores:
        if tab[a] == tab[b] == tab[c] == jugador1:
            return "Gano el jugador 1"
        elif tab[a] == tab[b] == tab[c] == jugador2 or tab[a] == tab[b] == tab[c] == Computadora:
            if tipo_de_juego == "1":  
                return "Gano el jugador 2"
            else:  
                return "Gano la computadora"
    for i in tab:
        if i != jugador1 and i != jugador2 and i != Computadora:
            break
    else:
        return "Empate"
    return None
 
def jvsj():
    reiniciar_tablero()
    while True:        
        limpiar_terminal()
        imprimir_tablero(tab)
        eleccion_del_jugador1(tab)
        resultado = verificar_ganador(tab)
        if resultado is not None:
            limpiar_terminal()
            imprimir_tablero(tab)
            print(resultado) 
            break
        limpiar_terminal()
        imprimir_tablero(tab)  
        eleccion_del_jugador2(tab)
        resultado = verificar_ganador(tab)
        if resultado is not None:
            limpiar_terminal()
            imprimir_tablero(tab)
            print(resultado)
            break 
        imprimir_tablero(tab)

def jvsc():
    reiniciar_tablero()
    while True:
            limpiar_terminal()
            imprimir_tablero(tab)
            eleccion_del_jugador1(tab)
            resultado = verificar_ganador(tab)
            if resultado is not None:
                limpiar_terminal()
                imprimir_tablero(tab)
                print(resultado) 
                break
            limpiar_terminal() 
            imprimir_tablero(tab)  
            eleccion_de_computadora(tab)
            resultado = verificar_ganador(tab)
            if resultado is not None:
                limpiar_terminal()
                imprimir_tablero(tab)
                print(resultado) 
                break
            imprimir_tablero(tab)         

while True:
    
    tipo_de_juego=menu()
    if tipo_de_juego=="1":
            jvsj()
    elif tipo_de_juego=="2":
            jvsc()            
    elif tipo_de_juego=="3":
            print("Adiosss")
            break
    nueva_partida=input("¿Deseas jugar una nueva partida? (si/no): ")
    if nueva_partida.lower()=="si":
        print("Comenzando nueva partida")
        reiniciar_tablero()
    else:
        print("Cerrando el programa")
        break 