
from django.http import  FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse


def toPdf(lines,name):
    buff = io.BytesIO()
	c = canvas.Canvas(buff, pagesize=letter, bottomup=0)
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont('Helvetica', 12)
	 



	for line in lines:
		textob.textLine(line)

	c.drawText(textob)
	c.showPage()
	c.save()
	buff.seek(0)
	return (buff)