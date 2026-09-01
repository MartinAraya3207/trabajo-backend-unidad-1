from django.shortcuts import render

from . import models


def index(request):
    return render(request, 'index.html')


def servicios(request):
    contexto = {'servicios': models.servicios}
    return render(request, 'servicios.html', contexto)


def detalle_servicio(request, id):
    servicio = next((s for s in models.servicios if s.id == id), None)
    contexto = {'servicio': servicio}
    return render(request, 'detalle.html', contexto)


def nosotros(request):
    return render(request, 'nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')
