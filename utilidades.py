def validacionEntradaUsuario(mensaje):
    #Validar que el usuario ingrese un maldito numero
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error, ingrese un número válido")