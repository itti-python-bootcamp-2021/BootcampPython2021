import unittest
from borrar import *

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5,2),7)
    def test_restar(self):
        self.assertEqual(restar(5,2),3)

if __name__=="__main__":
    unittest.main()