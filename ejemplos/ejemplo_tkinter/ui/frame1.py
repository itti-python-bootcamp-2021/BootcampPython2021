import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import LEFT
from persistencia.gestor_peliculas import GestorBBDD
from ui_core.simple_gui_components import SuperFrame
from model.pelicula import Pelicula
import logging

class Frame1(SuperFrame):
    #Botones
    BUTTONS_WIDTH=200
    BUTTONS_HEIGHT=50
    buttons_images=[]
    #Color de fondo
    BG_COLOR = "pink"
    def __init__(self, parent, width, height):
        SuperFrame.__init__(self, parent, bg=self.BG_COLOR, width=width, height=height)

        #Botones para la toolbar
        buttons = (
            ("Refrescar",self.refrescar,None),
            ("Guardar",self.guardar,"icons/save.png"),
            ("Cancelar",self.cancelar,"icons/cancel.png")
        ) 
        self.createToolbar(buttons, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)
        #Componentes de la GUI
        self.label_titulo = tk.Label(self, text="Titulo:", background=self.BG_COLOR)
        self.label_titulo.place(x=50,y=100)
        self.entry_titulo = tk.Entry(self, width=50)
        self.entry_titulo.place(x=140, y=100)

        self.label_director = tk.Label(self, text="Director:", background=self.BG_COLOR)
        self.label_director.place(x=50,y=130)
        self.entry_director = tk.Entry(self, width=50)
        self.entry_director.place(x=140, y=130)

        self.label_anyo = tk.Label(self, text="Año estreno:", background=self.BG_COLOR)
        self.label_anyo.place(x=50,y=160)
        self.entry_anyo = tk.Entry(self, width=25)
        self.entry_anyo.place(x=140, y=160)


        self.pack()

    def refrescar(self):
        print("Resfrescando...")
    
    def guardar(self):
        print("Guardando...")

        titulo = self.entry_titulo.get() #Obtiene el texto que hay en la caja de texto del título
        director = self.entry_director.get()
        anyo = int(self.entry_anyo.get())
        pelicula = Pelicula(0, titulo, director, anyo, None)
        try:
            gestor = GestorBBDD()
            gestor.create(pelicula)
            tk.messagebox.showinfo(title="Movie Manager", message="La película se ha creado satisfactoriamente") 
        except Exception as e:
            logging.error(e)
            tk.messagebox.showerror(title="Movie Manager", message="Error al crear la película")

    def cancelar(self):
        print("Cancelando...")
    