'''
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

def infoPersonal():
    datosPersonales = {}
    continuar = True
    while continuar == True:
        clave = input("¿Que dato desea introducir?: ")
        valor = input("Introduzca su " + str(clave) + ": ")
        datosPersonales[clave] = valor
        continuar = input("¿Algo más que añadir?(Si/No): ")
        if continuar == "No":
            continuar = False
        elif continuar == "Si":
            continuar = True
    return datosPersonales



if __name__ == "__main__":
    

    #Entrada
    entrada = infoPersonal()

    #Proceso

    #Salida
    print(entrada)