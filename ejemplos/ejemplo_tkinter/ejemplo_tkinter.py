import tkinter

def calcular(event):
    print("Calculando...")
    print(text_input.get("1.0","end-1c"))

def cambiar_color(event):
    print("Cambiando color...")

ventana = tkinter.Tk()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ANCHO_VENTANA = 1024
ALTO_VENTANA = 768
OFFSET_X = int((ancho_pantalla - ANCHO_VENTANA) / 2)
OFFSET_Y = int((alto_pantalla - ALTO_VENTANA) / 2)
ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}+{OFFSET_X}+{OFFSET_Y}")
ventana.resizable(False, False)
ventana.title("Gestor de Facturas v.1.0")

text_input = tkinter.Text()
text_input.pack()
boton = tkinter.Button(height=10, width=10, text="Púlsame", borderwidth=10, bg='#4a7abc')
boton.bind("<Button-1>",calcular)
boton.bind("<Button-2>",cambiar_color)
boton.pack()

ventana.mainloop()
