from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="get_file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 40)
    p.drawString(10,600, "Hello, I am Kushal Neupane.")
    p.showPage()
    p.save()
    return response