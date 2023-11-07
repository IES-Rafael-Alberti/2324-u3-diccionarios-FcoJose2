from src.Ejercicio5 import suma, mensajeSalidaA, mensajeSalidaB

def test_suma():
    assert suma({'Matemáticas': 6, 'Física': 4, 'Química': 5}) == 15

def test_mensajeSalidaA():
    assert mensajeSalidaA({'Matemáticas': 6, 'Física': 4, 'Química': 5}) == ['Matemáticas tiene 6 creditos.', 'Física tiene 4 creditos.', 'Química tiene 5 creditos.']

def test_mensajeSalidaB():
    assert mensajeSalidaB(['Matemáticas tiene 6 creditos.', 'Física tiene 4 creditos.', 'Química tiene 5 creditos.'], 15) == "Matemáticas tiene 6 creditos.\nFísica tiene 4 creditos.\nQuímica tiene 5 creditos.\nLos creditos totales son: 15"