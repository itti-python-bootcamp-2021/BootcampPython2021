import tkinter as tk

class Frame1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="pink", width=1024, height=768)
        entry_nombre = tk.Entry(self)
        entry_nombre.place(x=50, y=50)
        self.pack()