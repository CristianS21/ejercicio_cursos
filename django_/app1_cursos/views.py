from django.http import HttpResponse
from django.shortcuts import render
from app1_cursos.forms import curso_formulario 


def inicio (request):
    return render (request, "app_1/inicio.html")

def cursos (request):
    return render (request, "app_1/cursos.html")

def cursos_formulario (request):
    if request.method=="post":
        formulario=curso_formulario(request.post)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = curso (nombre=data["nombre"], comision=data["comision"])
            curso.save()
            return render (request, "app_1/inicio.html")
      
    else:
        formulario=curso_formulario()
    return render (request, "app_1/form_cursos.html", {"formulario": formulario})





def profesores (request):
    return render (request, "app_1/profesores.html")

def estudiantes (request):
    return render (request, "app_1/estudiantes.html")

def entregables (request):
    return render (request, "app_1/entregables.html")
