from src.Ejercicio2 import datosPersonales, mensajeSalida

def test_datosPersonales():
    assert datosPersonales("Juan","18","Cádiz","4232325252") == {'nombre':"Juan","edad":"18","dirección":"Cádiz","telefono":"4232325252"}
def test_mensajeSalida():
    assert mensajeSalida({'nombre':"Juan","edad":"18","dirección":"Cádiz","telefono":"4232325252"}) == "Juan tiene 18 años, vive en Cádiz y su número de teléfono es 4232325252."