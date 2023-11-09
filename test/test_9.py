from src.Ejercicio9 import mensajeSalida, gestionFacturas

def test_gestionFacturas(monkeypatch):
    entrada = ["A","1","100","P","1","T"]
    def mock_input(s):
        return entrada.pop(0)
    monkeypatch.setattr("builtins.input", mock_input)
    assert gestionFacturas(["A","1","100","P","1","T"]) == (100,0)

def test_mensajeSalida():
    assert mensajeSalida(100,0) == "Cantidad pagada: 100\nPendiente de pagar: 0"