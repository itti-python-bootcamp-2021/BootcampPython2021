"""
Clase Empleado - Nombre - Categoría (Director, Ingeniero, Programador) - Salario
Crear 5 empleados.
Filtro que nos proporcione todos los ingenieros
Filtro que nos proporcione todos los nombres que empiecen por R
Filtro que nos proporcione todos empleados cuyo salario es <20000
NIVEL NINJA: Comprobar en el filtro que no se cuela algo que no sea Empleado.
"""
class Empleado:
    def __init__(self, nombre, categoria, salario) -> None:
        self.nombre = nombre
        self.categoria = categoria
        self.salario = salario

    def __str__(self) -> str:
        return (f"Nombre {self.nombre}:Categoría {self.categoria}:Salario {self.salario}")

    #Se puede implementar la función de filtrado como un método de clase
    @classmethod
    def filtro_salario(cls, empleado):
        return (empleado.salario<20000)

e1 = Empleado("Nombre  1","Director",30000)
e2 = Empleado("Nombre  2","Ingeniero",30000)
e3 = Empleado("Ramón  3","Programador",18000)
e4 = Empleado("Nombre  4","Ingeniero",19000)
e5 = Empleado("Raúl  5","Ingeniero",30000)
empleados = [e1,e2,e3,e4,e5]

def filtro_ingenieros(empleado):
    return (empleado.categoria=="Ingeniero")

def filtro_nombre_r(empleado):
    return (empleado.nombre.startswith("R"))

def filtro_salario(empleado):
    return (empleado.salario<20000)

empleados_ingenieros = filter(Empleado.filtro_salario, empleados)
for empleado in empleados_ingenieros:
    print(empleado)