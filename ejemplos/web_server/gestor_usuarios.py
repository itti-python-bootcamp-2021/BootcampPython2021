class Usuario:
    def __init__(self, email, pwd) -> None:
        self.email = email
        self.pwd = pwd

    def store(self):
        with open("usuarios.txt","a",encoding="UTF-8") as fichero_usuarios:
            fichero_usuarios.write(self.email + "#" + self.pwd + "\n")
