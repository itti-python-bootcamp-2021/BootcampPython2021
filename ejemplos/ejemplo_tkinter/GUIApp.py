import logging
import sys
from tkinter import *
import tkinter.messagebox
from ui.frame1 import Frame1
from ui.frame2 import Frame2
from ui.frame3 import Frame3

class GUIApp:
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 768
    APP_TITLE = "Gestor de Facturas v.1.0"
    app = Tk()
    frames = {}

    # Constructor
    def __init__(self) -> None:
        self.init_window()
        self.init_menu()
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
        self.app.title(self.APP_TITLE)

    # Construcción del menú
    def init_menu(self):
        logging.debug("Entrando en init_menu")
        menubar = Menu(self.app)
        menu_archivo = ("Archivo", (("Nuevo", self.prueba), ("Abrir",),
            ("Guardar",), ("Cerrar",), None, ("Salir", self.exit)))
        menu_editar = ("Editar", (("Cortar",), ("Copiar",), ("Pegar",)))
        menu_ventanas = ("Peliculas", 
            (
                ("Crear",self.mostrarFrame1),
                ("Consultar",self.mostrarFrame2),
                ("Borrar",self.mostrarFrame3)
        ))
        menu_ayuda = ("Ayuda", (("Ayuda",), None, ("Acerca de...", self.about)))
        menus = (menu_archivo, menu_editar, menu_ventanas, menu_ayuda)
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

    #Inicialización de las "pantallas" (Frames) de la aplicación
    def init_frames(self):
        logging.debug("Entrando en init_frames")
        self.frames["Frame1"]=Frame1(self.app, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.frames["Frame2"]=Frame2(self.app, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.frames["Frame3"]=Frame3(self.app, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.mostrarFrame1()

    #Cambio de Frame 
    def showFrame(self, frameName):
        logging.debug("Entrando en mostrarFrame")
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frameName].pack()
    
    def mostrarFrame1(self):
        logging.debug("Entrando en mostrarFrame1")
        self.showFrame("Frame1")
    
    def mostrarFrame2(self):
        logging.debug("Entrando en mostrarFrame2")
        self.showFrame("Frame2")
    
    def mostrarFrame3(self):
        logging.debug("Entrando en mostrarFrame3")
        self.showFrame("Frame3")
        
    def exit(self):
        logging.debug("Entrando en exit")
        sys.exit()

    def prueba(self):
        logging.debug("Entrando en prueba")

    def about(self):
        logging.debug("Entrando en About...")
        tkinter.messagebox.showinfo(title="Python Simple GUI Framework", message="Fernando Paniagua (2021)\nfernando.paniagua.formacion@gmail.com")

if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    app = GUIApp()
