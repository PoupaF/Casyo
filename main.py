from figuras_2d import * #importa codigo que no tenemos en el main
from utilidades import *

def menuPrincipal():
    #Menu Principal
    print("\n--- Calculadora Geométrica---")
    print("Seleccione un valor númerico para comenzar:")
    print(" 01-Figuras 2D")
    print(" 99-Salir")

def menuFiguras_2d():
    #Menu de las figuras bidimensionales
    print("\n---Figuras 2D---")
    print("Seleccione un valor para continuar:")
    print(" 01-Cuadrado")
    print(" 02-Rectangulo")
    print(" 03-Circulo")
    print(" 04-Triangulo")

def main():
    #Funcion principal en bicle
    while True:
        menuPrincipal() #Mostrar el menu principal
        EntradaNumericaUsuario = validacionEntradaUsuario("elige un número: ")
        
        if EntradaNumericaUsuario == 1:
            #ejecutar código de figuras bidimensionales
            print("ejecutando bidimensionales")

        elif EntradaNumericaUsuario == 99:
            print("bays")
            break

if __name__ == "__main__":
    main()