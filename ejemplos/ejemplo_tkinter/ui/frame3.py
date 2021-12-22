import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import LEFT
from ui_core.simple_gui_components import SimpleTable
from ui_core.simple_gui_components import SuperFrame

class Frame3(SuperFrame):
    #Botones
    BUTTONS_WIDTH=100
    BUTTONS_HEIGHT=50
    buttons_images=[]
    #Color de fondo
    BG_COLOR = "yellow"
    def __init__(self, parent, width, height):
        SuperFrame.__init__(self, parent, bg=self.BG_COLOR, width=width, height=height)
        #Botones para la toolbar
        buttons = (
            ("Nuevo",self.crear,None),
            ("Viejo",self.leer,None)
        ) 
        self.createToolbar(buttons, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)

        self.pack()      
    
    def crear(self):
        print("Creando...")
        
    def leer(self):
        print("Leyendo...")
    