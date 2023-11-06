'''
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

def devolverSimbolo(divisas, divisaPedida):
    if divisaPedida in divisas:
        mensaje = "El simbolo de la divisa es: " + divisas[divisaPedida]
    else:
        mensaje = "Introduce una divisa correcta"
    return mensaje



if __name__ == "__main__":
    

    #Entrada
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisaPedida = input("Introduce una divisa(Euro, Dollar o Yen): ")
    #Proceso
    mensaje = devolverSimbolo(divisas,divisaPedida)
    #Salida
    print(mensaje)

