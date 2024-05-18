from django.shortcuts import render

from . import models

def index(request):
    consulta = models.Sede.objects.all()
    contexto = {"sedes" : consulta}
    return render(request, "Clinica/index.html", contexto)
    