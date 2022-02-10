import numpy as np
import timeit

print(np.zeros(100))#Lista con 100 ceros
print(np.ones(100, dtype=np.intc))#Lista con 100 unos de type intc
print(np.full(100,5))#Lista de 100 cincos (enteros)

setup_python = """
lista_python = list(range(0,10_000))
"""

tiempo_python = timeit.timeit(setup=setup_python, stmt="sum(lista_python)", number=10_000)
print(f"Tiempo empleado: {tiempo_python}")

setup_numpy = """
import numpy as np
lista_python = list(range(0,10_000))
array_numpy = np.array(lista_python) # Transformación de una lista de Python a np.array
"""

tiempo_numpy = timeit.timeit(setup=setup_numpy, stmt="np.sum(array_numpy)", number=10_000)
print(f"Tiempo empleado: {tiempo_numpy}")

tiempo_python = timeit.timeit(stmt="list(range(10000))", number=1000)
tiempo_numpy = timeit.timeit(setup="import numpy as np", stmt="np.arange(10000)", number=1000)
print(f"Tiempo Python: {tiempo_python}")
print(f"Tiempo Numpy: {tiempo_numpy}")

print(np.arange(10)) #Números del 0 al 9
print(np.arange(10,20)) #Números del 10 al 19
print(np.arange(10,20,2)) #Números del 10 al 19 de 2 en 2
print(np.arange(100,20,-2)) #Números del 100 al 20 de -2 en -2

print(np.full((3,3),np.pi))
"""
[[3.14159265 3.14159265 3.14159265]
 [3.14159265 3.14159265 3.14159265]
 [3.14159265 3.14159265 3.14159265]]
"""

print(np.linspace(2,100,50)) #50 interpolaciones equidistantes entre 2 y 100
"""
[  2.   4.   6.   8.  10.  12.  14.  16.  18.  20.  22.  24.  26.  28.
  30.  32.  34.  36.  38.  40.  42.  44.  46.  48.  50.  52.  54.  56.
  58.  60.  62.  64.  66.  68.  70.  72.  74.  76.  78.  80.  82.  84.
  86.  88.  90.  92.  94.  96.  98. 100.]
"""

np.random.random((3,3))
"""
array([[0.20081124, 0.95330031, 0.09671294],
       [0.99620383, 0.62963392, 0.18480751],
       [0.29317465, 0.37395839, 0.62447556]])"""