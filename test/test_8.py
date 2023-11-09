from src.Ejercicio8 import traducir, crearDiccionario

def test_crearDiccionario():
    assert crearDiccionario("hola:hello,mundo:world") == {"hola":"hello","mundo":"world"}

def test_traducir(monkeypatch):
    diccionario = {"hola":"hello","mundo":"world"}
    input_values = "hola mundo"
    def mock_input(s):
        return input_values
    monkeypatch.setattr("builtins.input",mock_input)
    assert traducir(diccionario) == "hello world"