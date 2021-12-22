import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import LEFT
from ui_core.simple_gui_components import SimpleTable
from ui_core.simple_gui_components import SuperFrame
from persistencia.gestor_peliculas import GestorBBDD

class Frame2(SuperFrame):
    #Botones
    BUTTONS_WIDTH=100
    BUTTONS_HEIGHT=50
    buttons_images=[]
    #Tabla
    TABLE_WIDTH = 1000
    ROWS_HEIGHT = 15
    TABLE_X_POS = 10
    TABLE_Y_POS = 80
    #Color de fondo
    BG_COLOR = "blue"
    def __init__(self, parent, width, height):
        SuperFrame.__init__(self, parent, bg=self.BG_COLOR, width=width, height=height)
        #Botones para la toolbar
        buttons = (
            ("Recargar",self.recargar,None),
        ) 
        self.createToolbar(buttons, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)

        #Tabla
        columns_ids = tuple(range(1,5))
        columns_names = ("ID","Título","Director","Año")

        self.table = SimpleTable(self, columns_ids=columns_ids, columns_names=columns_names, table_with=self.TABLE_WIDTH, rows_height=self.ROWS_HEIGHT)

        self.table.place(x=self.TABLE_X_POS, y=self.TABLE_Y_POS)
        self.pack()      
    
    def recargar(self):
        print("Recargando...")
        #Borramos la tabla
        for i in self.table.get_children():
            self.table.delete(i)
        #Instanciamos el gestor de persistencia
        gestor = GestorBBDD()

        #Obtenemos todas las películas
        lista_peliculas = gestor.findAll()
        #Pasamos las películas a la tabla        
        self.table.insert_rows(lista_peliculas)        