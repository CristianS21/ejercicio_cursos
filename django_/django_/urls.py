from django_.views import probar_plantilla
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', probar_plantilla)
]
