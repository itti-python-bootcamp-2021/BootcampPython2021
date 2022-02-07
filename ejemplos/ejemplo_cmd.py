from cmd import Cmd

class GestorComandos(Cmd):
    def do_saludar(self, nombre):
        print ("Hola", nombre)

    def do_fin(self, args):
        print ("Finalizando...")
        raise SystemExit

if __name__ == '__main__':
    gestor = GestorComandos()
    gestor.prompt = '>'
    gestor.cmdloop('Ready')