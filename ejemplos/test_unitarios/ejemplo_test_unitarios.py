import unittest
from programa import *

class ProbadorPrograma(unittest.TestCase):
    contador = 0
    lista = [1,2,3,4,5]
    @classmethod
    def setUpClass(cls) -> None:
        print("ABRIENDO CONEXIÓN CON LA BASE DE DATOS:" + str(cls.contador))

    @classmethod
    def tearDownClass(cls) -> None:
        print("CERRANDO LA CONEXIÓN CON LA BASE DE DATOS. Contador:" + str(cls.contador))

    def setUp(self) -> None:
        print("RESTAURANDO:" + str(ProbadorPrograma.contador))
        ProbadorPrograma.lista = [1,2,3,4,5]

    def tearDown(self) -> None:
        return super().tearDown()
    def test_saludar(self):
        self.skipTest("NADA")
        ProbadorPrograma.contador+=1
        self.assertEqual("Hola",saludar())
    def test_sumar(self):
        self.skipTest("NADA")
        ProbadorPrograma.contador+=1
        self.assertEqual(4,sumar(2,2))
        self.assertEqual(-1,sumar(2,-3))
        self.assertEqual(-8,sumar(-4,-4))
    def test_dividir(self):
        self.skipTest("NADA")
        ProbadorPrograma.contador+=1
        self.assertEqual(5,dividir(10,2))
        self.assertEqual(-5,dividir(-10,2))
        self.assertEqual(4.5,dividir(9,2))
    def test_esta_en_la_lista(self):
        self.skipTest("NADA")
        ProbadorPrograma.contador+=1
        self.assertFalse(esta_en_la_lista("elemento-que-no-esta-en-la-lista"))
    def test_animal(self):
        self.skipTest("NADA")
        ProbadorPrograma.contador+=1
        #Si la longitud es PAR es un error.
        a = Animal("Gato",4)
        longitud = a.get_longitud()
        es_par = (longitud%2==0)
        if (es_par):
            self.fail("El número de patas es PAR")
    def test_get_lista(self):
        self.skipTest("NADA")
        ProbadorPrograma.contador+=1
        self.assertListEqual(["uno","dos","cuatro"],get_lista())

    def test_dividir_exception(self):
        self.assertRaises(MiZeroException, dividir(10,0))

if __name__ == '__main__':
    unittest.main()