from django.urls import path
from app1_cursos import views 

urlpatterns = [

    path('inicio/', views.inicio, name="inicio"),
    path('posteo/', views.posteo, name="posteo"),
    path('principal/', views.principal, name="principal")  
]

