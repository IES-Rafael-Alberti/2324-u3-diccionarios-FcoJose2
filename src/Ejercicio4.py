'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
'''


def separarFecha(fecha):
    fechaS = fecha.split("/")
    return fechaS


def mensajeSalida(fechaS,  meses):
    mensaje = fechaS[0] + " de " + meses[fechaS[1]] + " " + fechaS[2]
    return mensaje


if __name__ == "__main__":
    

    #Entrada

    fecha = input("Introduce una fecha (formato dd/mm/aaaa): ")
    meses = {"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"}
    #Proceso
    fechaS = separarFecha(fecha)
    mensaje = mensajeSalida(fechaS, meses)
    #Salida
    print(mensaje)

