from src.Ejercicio4 import separarFecha, mensajeSalida

def test_separarFecha():
    assert separarFecha("03/12/2004") == ['03', '12', '2004']

def test_mensajeSalida():
    assert mensajeSalida(['03', '12', '2004'], {"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"}) == "03 de diciembre 2004"