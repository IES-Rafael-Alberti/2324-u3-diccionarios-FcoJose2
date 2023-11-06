from src.Ejercicio3 import calcularPrecios, mensajeSalida

def test_calcularPrecios():
    assert calcularPrecios({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"manzana",3) == 2.4

def test_mensajeSalida():
    assert mensajeSalida(2.4,"manzana",{"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70})  == "El coste total es de: 2.4"