from django.shortcuts import render
from app1_cursos.models import Posteo
from app1_cursos.forms import posteo_formulario

def inicio (request):
    return render (request, "app_1/inicio.html")

def posteo (request):
    if request.method =='POST':

        formulario= posteo_formulario (request.POST,request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            posteo1= Posteo (imagen= data ['imagen'],fecha =data['fecha'], autor=data['autor'], descripcion=data['descripcion'], )
            posteo1.save()

        return render(request, "app_1/plantilla_principal.html")
    else:  
        formulario= posteo_formulario()  # Formulario vacio para construir el html
    return render(request, "app_1/form_posteo.html", {"formulario": formulario})

def principal (request):
    posteos = Posteo.objects.all()
    contexto= {"posteos":posteos}
    return render (request, "app_1/plantilla_principal.html", contexto)