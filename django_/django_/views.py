from django.http import HttpResponse
from django.template import Template, Context, loader
from app1_cursos.models import Curso


def probar_plantilla (request):
    consulta = Curso.objects.all()
    diccionario= {"cursos":consulta}
    plantilla_1=loader.get_template("plantilla_1.html")
    documento_html= plantilla_1.render (diccionario)
    return HttpResponse(documento_html)





    