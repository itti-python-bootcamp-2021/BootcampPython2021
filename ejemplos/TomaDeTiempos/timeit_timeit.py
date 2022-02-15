import timeit

setup_code = "lista = list(range(1,10000))"
code = """
for l in lista:
    print(l)
"""

print(timeit.timeit(stmt=code, setup=setup_code, number=10))
