class CV(object):
    def __init__(self, nombre, direccion, telefono, email) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.experiencias = []
        self.contacto = CV.Contacto(telefono,email)

    def mostrar(self) -> str:
        print(self.nombre + ":" +self.direccion)
        print(self.contacto)
        for experiencia in self.experiencias:
            print(experiencia)

    def agregar_objeto_experiencia(self, experiencia):
        self.experiencias.append(experiencia)

    def agregar_experiencia(self, empresa, puesto):
        self.experiencias.append(CV.ExperienciaProfesional(empresa,puesto))

    class ExperienciaProfesional():
        def __init__(self, empresa, puesto, duracion=0) -> None:
            self.empresa = empresa
            self.puesto = puesto
            self.duracion = duracion
        def __str__(self) -> str:
            return self.empresa+":"+self.puesto

    class Contacto():
        def __init__(self, telefono, email) -> None:
            self.telefono = telefono
            self.email = email
        
        def __str__(self) -> str:
            return self.telefono+":"+self.email

cv_jl = CV(
    "Juan Luis Roca",
    "Barcelona",
    "937910101",
    "jlr@gmail.com")
cv_jl.agregar_objeto_experiencia(CV.ExperienciaProfesional("Autónomo","Consultor"))
cv_jl.agregar_experiencia("IBM","Formador")
cv_jl.agregar_objeto_experiencia(CV.ExperienciaProfesional("RHENUS","Programador"))
cv_jl.mostrar()