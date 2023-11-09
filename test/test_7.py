from src.Ejercicio7 import sumarCesta

def test_sumarCesta():
    assert sumarCesta({"tostadora":50,"bañera":499}) == "El coste total es: 549"