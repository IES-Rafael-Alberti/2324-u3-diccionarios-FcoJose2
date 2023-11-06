'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
'''
def calcularPrecios(productos, frutaPedida, kilosPedidos):
    
    if frutaPedida in productos:
        precio = round((productos[frutaPedida] * kilosPedidos),2)
    else:
        precio = "Introduce una fruta correcta"
    return precio

def mensajeSalida(precio, frutaPedida, productos):
    if frutaPedida in productos:
        mensaje = "El coste total es de: " + str(precio)
    else:
        mensaje = precio
    return mensaje


if __name__ == "__main__":
    

    #Entrada
    productos = {"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
    frutaPedida = input("¿Qué fruta quieres? (Plátano, Manzana, Pera, Naranja): ")
    frutaPedida = frutaPedida.lower()
    kilosPedidos = int(input("Introduce la cantidad (en Kg) deseada: "))
    #Proceso
    
    precio =  calcularPrecios(productos, frutaPedida, kilosPedidos)
    mensaje = mensajeSalida(precio, frutaPedida, productos)
    #Salida
    print(mensaje)

