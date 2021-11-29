import logging
import sys
from tkinter import *
from gestor_eventos import *


class GUIApp:
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 768
    app = Tk()

    # Constructor
    def __init__(self) -> None:
        self.init_window()
        self.init_menu()
        # self.init_components()
        self.init_frames()
        self.app.mainloop()

    # Construcción de la ventana
    def init_window(self):
        logging.debug("Entrando en create_window")
        ancho_pantalla = self.app.winfo_screenwidth()
        alto_pantalla = self.app.winfo_screenheight()
        OFFSET_X = int((ancho_pantalla - self.WINDOW_WIDTH) / 2)
        OFFSET_Y = int((alto_pantalla - self.WINDOW_HEIGHT) / 2)
        self.app.geometry(
            f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{OFFSET_X}+{OFFSET_Y}")
        self.app.resizable(False, False)
        self.app.title("Gestor de Facturas v.1.0")

    # Construcción del menú
    def init_menu(self):
        logging.debug("Entrando en init_menu")
        menubar = Menu(self.app)
        menu_archivo = ("Archivo", (("Nuevo", self.prueba), ("Abrir",),
                        ("Guardar",), ("Cerrar",), None, ("Salir", self.exit)))
        menu_editar = ("Editar", (("Cortar",), ("Copiar",), ("Pegar",)))
        menu_ayuda = ("Ayuda", (("Ayuda",), None, ("Acerca de...",)))
        menus = (menu_archivo, menu_editar, menu_ayuda)
        self.app.config(menu=menubar)
        for menu in menus:
            nuevo_menu = Menu(menubar, tearoff=0)
            for opcion in menu[1]:
                if opcion == None:
                    nuevo_menu.add_separator()
                else:
                    if (len(opcion) == 1):
                        nuevo_menu.add_command(label=opcion[0])
                    else:
                        nuevo_menu.add_command(
                            label=opcion[0], command=opcion[1])
                        print(opcion[1])
            menubar.add_cascade(label=menu[0], menu=nuevo_menu)

    # Construcción de los componentes
    def init_components(self):
        logging.debug("Entrando en create_components")
        text_input = Text()
        text_input.pack()
        boton = Button(height=10, width=10, text="Púlsame",
                       borderwidth=10, bg='#4a7abc')
        # boton.bind("<Button-1>",calcular())
        boton.pack()

    def init_frames(self):
        logging.debug("Entrando en init_frames")
        frame1 = Frame(self.app, bg="green",
                       width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        frame1.pack()
        frame2 = Frame(self.app, bg="pink",
                       width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        frame2.pack()

        # boton = Button(frame1, height=10, width=10, text="Púlsame", borderwidth=10, bg='#4a7abc')
        # boton.bind("<Button-1>",calcular())
        # boton.pack()

    def exit(self):
        logging.debug("Entrando en exit")
        sys.exit()

    def prueba(self):
        logging.debug("Entrando en prueba")

if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    app = GUIApp()