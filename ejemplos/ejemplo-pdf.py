#pip install FPDF
from fpdf import FPDF
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 10)
pdf.set_text_color(255, 0, 0)
pdf.text(100, 100, "Ejemplo de generación de PFD")
pdf.output('salida.pdf')