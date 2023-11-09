'''
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''


def crearDiccionario(entrada):
    diccionario = {}
    for i in entrada.split(","):
        p_espa, p_ingles = i.split(":")
        diccionario[p_espa] = p_ingles    
    return diccionario


def traducir(diccionario):
    resultado = []
    frase = input("Introduce la frase a traducir: ")

    for i in frase.split():
        if i in diccionario:
            resultado.append(diccionario[i])
        else:
            resultado.append(i)
    
    resultado = " ".join(resultado)
    return resultado

if __name__ == "__main__":
    

    #Entrada
    entrada = input("Intoduce la palabra y su traducción separada por (:), separando las palabras por comas (hola:hello,mundo:world): ")


    #Proceso
    diccionario = crearDiccionario(entrada)
    mensaje = traducir(diccionario)
    #Salida
    print(mensaje)