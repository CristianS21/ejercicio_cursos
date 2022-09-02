from django.http import HttpResponse
from django.shortcuts import render


def inicio (request):
    return render (request, "app_1/inicio.html")

def cursos (request):
    return render (request, "app_1/cursos.html")

def profesores (request):
    return render (request, "app_1/profesores.html")

def estudiantes (request):
    return render (request, "app_1/estudiantes.html")

def entregables (request):
    return render (request, "app_1/entregables.html")
