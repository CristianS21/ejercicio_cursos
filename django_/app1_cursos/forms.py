from unittest.util import _MAX_LENGTH
from django import forms

from app1_cursos.models import Posteo

class posteo_formulario (forms.Form):
    imagen= forms.ImageField()
    fecha=forms.DateField()
    autor=forms.CharField(max_length=250)
    descripcion=forms.CharField(max_length=250)

    class Meta:
        model = Posteo
        fields = ['imagen']


  