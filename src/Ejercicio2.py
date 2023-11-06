'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

def datosPersonales(nombre, edad, direccion, telefono):
    datos = {"nombre":nombre, "edad":edad, "dirección":direccion, "telefono":telefono}
    return datos

def mensajeSalida(datos):
    mensaje = datos["nombre"] + " tiene " + datos["edad"] + " años, vive en " + datos["dirección"] + " y su número de teléfono es " + datos["telefono"] + "."
    return mensaje

if __name__ == "__main__":
    

    #Entrada
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce su edad: ")
    direccion = input("Introduce su dirección: ")
    telefono = str(input("Introduce su telefono: "))
    #Proceso
    datos = datosPersonales(nombre, edad, direccion, telefono)
    mensaje = mensajeSalida(datos)
    #Salida
    print(mensaje)
