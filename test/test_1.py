from src.Ejercicio1 import devolverSimbolo

def test_devolverSimbolo():
    assert devolverSimbolo({'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, "Euro") == "El simbolo de la divisa es: €"
    assert devolverSimbolo({'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, "Yen") == "El simbolo de la divisa es: ¥"
    assert devolverSimbolo({'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, "Prueba") == "Introduce una divisa correcta"