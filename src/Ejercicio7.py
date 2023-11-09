'''
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
'''

def sumarCesta(cestaCompra):
    total = 0
    for producto,precio in cestaCompra.items():
        total += precio
    return "El coste total es: " + str(total)

def formatoCesta(cestaCompra):
    for producto,precio in cestaCompra.items():
        print(producto,"\t",precio)


if __name__ == "__main__":
    

    #Entrada
    cestaCompra = {}
    continuar = True
    while continuar == True:
        producto = input("Inroduzca el producto: ")
        precio = float(input("Introduzca el precio de " + str(producto) + ": "))
        cestaCompra[producto] = precio
        continuar = input("¿Algo más que añadir?(Si/No): ")
        if continuar == "No":
            continuar = False
        elif continuar == "Si":
            continuar = True
    #Proceso
    total = sumarCesta(cestaCompra)
    mensaje = formatoCesta(cestaCompra)
    #Salida
    print(total)
    print(mensaje)

