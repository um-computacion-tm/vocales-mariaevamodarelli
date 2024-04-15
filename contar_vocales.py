import unittest

def contar_vocales(el_string): 
    mi_string = el_string.lower()
    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
             if letra not in resultado: 
                     resultado[letra] = 0
             resultado[letra] += 1
    return resultado



class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales("zzz")
        self.assertEqual(resultado, {})

    def test_contar_1(self): 
        resultado = contar_vocales("cas")
        self.assertEqual(resultado, {"a": 1})

    def test_contar_2(self): 
        resultado = contar_vocales("casa")
        self.assertEqual(resultado, {"a": 2})

    def test_contar_3(self): 
        resultado = contar_vocales("bese")
        self.assertEqual(resultado, {"e": 2})

    def test_contar_4(self): 
        resultado = contar_vocales("besa")
        self.assertEqual(resultado, {"a": 1, "e": 1})

    def test_contar_5(self): 
        resultado = contar_vocales("casanova")
        self.assertEqual(resultado, {"a": 3, "o": 1})

    def test_contar_6(self): 
        resultado = contar_vocales("mUrciElago")
        self.assertEqual(resultado, {"a": 1, "u":1, "i":1, "e":1, "o":1})

    def test_contar_7(self): 
        resultado = contar_vocales("Avenida")
        self.assertEqual(resultado, {"a": 2, "e": 1, "i": 1})

    def test_contar_7(self): 
        resultado = contar_vocales("Emperador")
        self.assertEqual(resultado, {"a": 1, "e": 2, "o": 1})




unittest.main()

while(True):
    palabra = input("Ingrese palabra:")
    print(contar_vocales(palabra))
