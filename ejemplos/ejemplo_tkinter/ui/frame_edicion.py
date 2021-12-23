from logging import disable
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import DISABLED, END, LEFT
from ui_core.simple_gui_components import SimpleTable
from ui_core.simple_gui_components import SuperFrame
from persistencia.gestor_peliculas import GestorBBDD

class FrameEdicion(SuperFrame):
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
    BG_COLOR = None
    def __init__(self, parent, width, height):
        SuperFrame.__init__(self, parent, bg=self.BG_COLOR, width=width, height=height)
        #Botones para la toolbar
        buttons = (
            ("Actualizar",self.reload,"icons/refresh.png"),
            ("Borrar",self.delete,"icons/delete.png"),
            ("Editar",self.edit,"icons/edit.png"),
            ("Save",self.save,"icons/save.png"),            
            ("",self.create_pdf,"icons/pdf.png")
        ) 
        self.createToolbar(buttons, self.BUTTONS_WIDTH, self.BUTTONS_HEIGHT)

        self.init_components()

        self.pack()      
    
    def init_components(self):
        #Tabla
        columns_ids = tuple(range(1,5))
        columns_names = ("ID","Título","Director","Año")

        self.table = SimpleTable(self, columns_ids=columns_ids, columns_names=columns_names, table_with=self.TABLE_WIDTH, rows_height=self.ROWS_HEIGHT)
        self.table.place(x=self.TABLE_X_POS, y=self.TABLE_Y_POS)

        self.table.bind("<Double-1>", self.edit)

        #Datos
        self.label_id = tk.Label(self, text="Id:", background=self.BG_COLOR)
        self.label_id.place(x=300,y=450)
        self.entry_id = tk.Entry(self, width=50, state="readonly")
        self.entry_id.place(x=390, y=450)

        self.label_titulo = tk.Label(self, text="Titulo:", background=self.BG_COLOR)
        self.label_titulo.place(x=300,y=480)
        self.entry_titulo = tk.Entry(self, width=50)
        self.entry_titulo.place(x=390, y=480)

        self.label_director = tk.Label(self, text="Director:", background=self.BG_COLOR)
        self.label_director.place(x=300,y=510)
        self.entry_director = tk.Entry(self, width=50)
        self.entry_director.place(x=390, y=510)

        self.label_anyo = tk.Label(self, text="Año estreno:", background=self.BG_COLOR)
        self.label_anyo.place(x=300,y=540)
        self.entry_anyo = tk.Entry(self, width=25)
        self.entry_anyo.place(x=390, y=540)

    def reload(self):
        print("Recargando...")
        #Borramos la tabla
        self.table.clear_all()
        #Instanciamos el gestor de persistencia
        gestor = GestorBBDD()

        #Obtenemos todas las películas
        lista_peliculas = gestor.findAll()
        #Pasamos las películas a la tabla        
        self.table.insert_rows(lista_peliculas, 0)    

    def delete(self):
        print("Borrando...")
        if (self.table.get_selected_row_index()==""):
            tk.messagebox.showerror(title="Error", message="Debe seleccionar una película")
        else:
            row_index = int(self.table.get_selected_row_index())
            reply = tk.messagebox.askyesno(message="¿Está seguro de que desea eliminar la película?", title="Eliminar película")
            if (reply==True):
                gestor=GestorBBDD()
                gestor.delete(row_index)
                self.reload()
                tk.messagebox.showinfo(title="Aviso", message="La película se ha eliminado correctamente") 

    def edit(self, event=None):
        print("Editando...")
        if (self.table.get_selected_row_values()==""):
            tk.messagebox.showerror(title="Error", message="Debe seleccionar una película")
        else:
            selected_row = self.table.get_selected_row_values()
            self.set_entry_text(self.entry_id, selected_row[0])
            self.set_entry_text(self.entry_titulo, selected_row[1])
            self.set_entry_text(self.entry_director, selected_row[2])
            self.set_entry_text(self.entry_anyo, selected_row[3])
            
    def save(self):
        print("Guardando...")

    def create_pdf(self):
        print("Creando pdf...")