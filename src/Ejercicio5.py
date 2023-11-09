'''
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
'''
def suma(creditos):
    creditosTotales = 0
    for asignatura, credito in creditos.items():
        creditosTotales += credito
    return creditosTotales

def mensajeSalidaA(creditos):
    mensaje = []
    for asignatura, credito in creditos.items():
        mensaje.append(str(asignatura) + " tiene " + str(credito) + " creditos.")
    return mensaje

def mensajeSalidaB(mensaje, creditosTotales):
    mensaje = "\n".join(mensaje)
    return str(mensaje) + "\nLos creditos totales son: " + str(creditosTotales)






if __name__ == "__main__":
    

    #Entrada

    creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    #Proceso
    creditosTotales = suma(creditos)
    mensaje = mensajeSalidaA(creditos)
    mensaje = mensajeSalidaB(mensaje, creditosTotales)
    #Salida
    print(mensaje)


