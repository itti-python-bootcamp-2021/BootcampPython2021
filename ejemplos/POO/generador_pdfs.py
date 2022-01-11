from fpdf import FPDF

def generar_pdf(objeto, nombre_fichero):
    print("Generando pdf...")
    #GENERAR LA PÁGINA PDF
    pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    #GENERAMOS LOS DATOS
    atributos = dir(objeto)
    contador = 0
    for atributo in atributos:
        if (not str(atributo).startswith("__")):
            contador+=1
            pdf.text(10, 10*contador, (str(atributo)  + ":" + str(getattr(objeto, atributo))))
    pdf.output(nombre_fichero)
    pdf.close()
    