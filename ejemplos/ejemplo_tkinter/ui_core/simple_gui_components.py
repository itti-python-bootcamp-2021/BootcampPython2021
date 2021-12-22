from tkinter import *
from tkinter import ttk
from typing import Tuple
#https://pythonguides.com/python-tkinter-treeview/
#https://pythonguides.com/python-tkinter-table-tutorial/

class SimpleTable(ttk.Treeview):
    def __init__(self, frame, columns_ids, columns_names, table_with, rows_height):
        ttk.Treeview.__init__(self, frame, height=rows_height)

        #Cálculo del ancho de las columnas
        column_with = int(table_with/len(columns_ids))
        
        #Identificadores de las columnas
        self['columns']=columns_ids
        self.column("#0", width=0,  stretch=NO)
        for id in columns_ids:
            self.column(id,anchor=CENTER, width=column_with)
        
        #Títulos de las columnas
        self.heading("#0",text="",anchor=CENTER)
        for id, name in zip(columns_ids, columns_names):
            self.heading(id,text=name,anchor=CENTER)

        self.pack()

    def insert_rows(self, rows_values : Tuple):
        for row in rows_values:
            self.insert_row(row)
        
    def insert_row(self, row_values : Tuple):
        self.insert(parent='',index='end', values=row_values)

class SuperFrame(Frame):
    def __init__(self, parent, bg, width, height):
        Frame.__init__(self, parent, bg=self.BG_COLOR, width=width, height=height)

    def createToolbar(self, buttons, width, height):
        i = 0
        for button in buttons:
            if (button[2]!=None):
                button_image = PhotoImage(file=button[2]).subsample(4)
                self.buttons_images.append(button_image)
                new_button = ttk.Button(self, text=button[0],command=button[1],image=button_image,compound=LEFT)
            else:
                new_button = ttk.Button(self, text=button[0],command=button[1])
            new_button.place(x=i*width,y=0,width=width,height=height)
            i+=1