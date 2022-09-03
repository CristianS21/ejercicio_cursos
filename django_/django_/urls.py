from django_.views import probar_plantilla
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    #path('', admin.site.urls),
    #path('', probar_plantilla),
    path ("", include ("app1_cursos.urls")), 

]




