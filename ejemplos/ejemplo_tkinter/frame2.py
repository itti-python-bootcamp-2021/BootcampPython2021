import tkinter as tk

class Frame2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue", width=1024, height=768)
        self.pack()