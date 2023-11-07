from src.Ejercicio6 import infoPersonal
import pytest

def test_infoPersonal(monkeypatch):
    input_values_x = iter(["Edad", "18","Si","Nombre","Fran","No"])

    def mock_input(s):
        return next(input_values_x)
    monkeypatch.setattr("builtins.input",mock_input)
    assert infoPersonal() == {"Edad":"18","Nombre":"Fran"}