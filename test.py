from fpdf import FPDF
import subprocess

font_path = './font/unifont/'

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

fecha="AYSAM"

# add font
pdf.add_font('Simsun', '', font_path + 'SIMSUN.ttf', uni=True)

pdf.set_margins(0, 0, 0)

pdf.set_font('Arial', '', 7)
pdf.cell(166)
pdf.cell(0, 0, 'Reporte: DTECHR_0015', 0)

pdf.image('img/descarga-removebg-preview.png', 10, 10, 25)

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(18, 179, 179)
pdf.ln(15)
pdf.cell(65)
pdf.cell(0, 0, 'SOLICITUD DE VACACIONES', 0)

pdf.set_font('Arial', '', 8)
pdf.set_text_color(0, 0, 0)
pdf.ln(12)
pdf.cell(10)
pdf.cell(0, 0, 'Gerencia de Recursos', 0)
pdf.ln(3)
pdf.cell(17)
pdf.cell(0, 0, 'Humanos', 0)

pdf.set_font('Arial', '', 10)
pdf.ln(-4)
pdf.cell(160)
pdf.cell(0, 0, 'AYSAM /IE.02/PO.04/a', 0)

#hace los rectangulos
pdf.set_fill_color(200,200,200)
pdf.rect(x = 10, y = 46, w = 110, h = 8, style = 'DF')
pdf.rect(x = 120, y = 46, w = 80, h = 8, style = 'DF')
#define el tipo de letra, tamaño y color
pdf.set_font('Arial', 'B',12)
pdf.set_fill_color(110,110,110)
#imprime texto
pdf.ln(14)
pdf.cell(40)
pdf.cell(140, 0, 'APELLIDO Y NOMBRE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(150)
pdf.cell(140, 0, 'LEGAJO', 0)


#define el tipo de letra, tamaño y color
pdf.set_font('Arial', 'B',12)
#imprime texto
pdf.ln(10)
pdf.cell(40)
pdf.cell(140, 0, 'VARIABLE VARIABLE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(150)
pdf.cell(140, 0, 'VARIABLE', 0)

#hace los rectangulos
pdf.set_fill_color(200,200,200)
pdf.rect(x = 10, y = 70, w = 80, h = 8, style = 'DF')
pdf.rect(x = 90, y = 70, w = 60, h = 8, style = 'DF')
pdf.rect(x = 130, y = 70, w = 70, h = 8, style = 'DF')
#define el tipo de letra, tamaño y color
pdf.set_font('Arial', 'B',12)
pdf.set_fill_color(110,110,110)
#imprime texto
pdf.ln(14)
pdf.cell(22)
pdf.cell(140, 0, 'PERIODO DE VACACIONES', 0)
#imprime texto
pdf.ln(0)
pdf.cell(93)
pdf.cell(140, 0, 'TOTAL DE DIAS', 0)
#imprime texto
pdf.ln(0)
pdf.cell(135)
pdf.cell(140, 0, 'CORRESPONDEN AL AÑO', 0)

#define tipo de letra
pdf.set_font('Arial', 'B',12)
#imprime texto
pdf.ln(10)
pdf.cell(20)
pdf.cell(140, 0, 'DESDE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(60)
pdf.cell(140, 0, 'HASTA', 0)

#define tipo de letra
pdf.set_font('Arial', '',12)
#imprime texto
pdf.ln(8)
pdf.cell(18)
pdf.cell(140, 0, 'VARIABLE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(58)
pdf.cell(140, 0, 'VARIABLE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(104)
pdf.cell(140, 0, 'VARIABLE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(154)
pdf.cell(0, 0, 'VARIABLE', 0)

#hace los rectangulos
pdf.set_fill_color(200,200,200)
pdf.rect(x = 60, y = 110, w = 80, h = 8, style = 'DF')
#define tipo de letra
pdf.set_font('Arial', 'B',12)
#imprime texto
pdf.ln(22)
pdf.cell(66)
pdf.cell(140, 0, 'DEBE REANUDAR LAS TAREAS', 0)
#define tipo de letra
pdf.set_font('Arial', '',12)
#imprime texto
pdf.ln(10)
pdf.cell(88)
pdf.cell(140, 0, 'VARIABLE', 0)

#dibuja una linea
pdf.line(x1 = 15, y1 = 170, x2 = 100, y2 = 170)
pdf.line(x1 = 110, y1 = 170, x2 = 195, y2 = 170)

#define tipo de letra
pdf.set_font('Arial', '',12)
#imprime texto
pdf.ln(42)
pdf.cell(47)
pdf.cell(140, 0, 'VARIABLE', 0)
#define tipo de letra
pdf.set_font('Arial', 'B',12)
#imprime texto
pdf.ln(8)
pdf.cell(49)
pdf.cell(140, 0, 'FECHA', 0)
#imprime texto
pdf.ln(0)
pdf.cell(122)
pdf.cell(140, 0, 'FIRMA DEL COLABORADOR', 0)

#imprime texto
pdf.ln(15)
pdf.cell(8)
pdf.cell(0, 0, 'OBSERVACIONES:', 0)
#define tipo de letra
pdf.set_font('Arial', '',8)
#imprime texto
pdf.ln(5)
pdf.cell(8)
pdf.cell(0, 0, 'variable variable variable variable', 0)

#hace los rectangulos
pdf.set_fill_color(200,200,200)
pdf.rect(x = 10, y = 240, w = 124, h = 8, style = 'DF')
pdf.rect(x = 134, y = 240, w = 66, h = 8, style = 'DF')
#define el tipo de letra, tamaño y color
pdf.set_font('Arial', 'B',12)
pdf.set_fill_color(110,110,110)
#imprime texto
pdf.ln(50)
pdf.cell(50)
pdf.cell(0, 0, 'APROBADO', 0)
#imprime texto
pdf.ln(0)
pdf.cell(150)
pdf.cell(140, 0, 'VERIFICADO', 0)
#creamos rectangulos
pdf.rect(x = 10, y = 248, w = 62, h = 25, style = '')
pdf.rect(x = 72, y = 248, w = 62, h = 25, style = '')
pdf.rect(x = 134, y = 248, w = 66, h = 25, style = '')
#creamos rectangulos
pdf.rect(x = 10, y = 248, w = 62, h = 25, style = '')
pdf.rect(x = 72, y = 248, w = 62, h = 25, style = '')
pdf.rect(x = 134, y = 248, w = 66, h = 25, style = '')
#creamos rectangulos
pdf.rect(x = 10, y = 273, w = 62, h = 6, style = '')
pdf.rect(x = 72, y = 273, w = 62, h = 6, style = '')
pdf.rect(x = 134, y = 273, w = 66, h = 6, style = '')
#imprime texto
pdf.ln(32)
pdf.cell(35)
pdf.cell(140, 0, 'JEFE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(90)
pdf.cell(140, 0, 'GERENTE', 0)
#imprime texto
pdf.ln(0)
pdf.cell(140)
pdf.cell(130, 0, 'GERENCIA DE R.R.H.H.', 0)









pdf.output('prueba222.pdf', 'F')