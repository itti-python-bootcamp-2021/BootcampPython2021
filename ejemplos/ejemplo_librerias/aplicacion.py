"""
import calculadora
print(calculadora.sumar(3,4))
print(calculadora.restar(5,1))
"""
"""
import calculadora as calc

print(calc.sumar(3,4))
print(calc.restar(5,1))
"""
"""
from calculadora import sumar
print(sumar(10,2))
"""
from calculadora import sumar as suma_normal
from supercalculadora import sumar as suma_esteroides
from panilib import generador_numeros
print(generador_numeros.generar_numero())
print(suma_normal(3,8))
print(suma_esteroides(3,8))