from django.http import HttpResponse
from django.shortcuts import render
from app1_cursos.forms import curso_formulario 
from app1_cursos.models import Curso


def inicio (request):
    return render (request, "app_1/inicio.html")

def cursos (request):
    return render (request, "app_1/cursos.html")

def cursos_formulario (request):
    if request.method =="POST":
        formulario=curso_formulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso1 = Curso (nombre=data["nombre"], comision=data["comision"])
            curso1.save()
            return render (request, "app_1/inicio.html",{"exitoso":True})
      
    else:
        formulario=curso_formulario()
    return render (request, "app_1/form_cursos.html", {"formulario": formulario})





def profesores (request):
    return render (request, "app_1/profesores.html")

def estudiantes (request):
    return render (request, "app_1/estudiantes.html")

def entregables (request):
    return render (request, "app_1/entregables.html")
