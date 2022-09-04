from django_.views import probar_plantilla
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", include ("app1_cursos.urls")), 

]




