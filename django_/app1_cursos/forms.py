from unittest.util import _MAX_LENGTH
from django import forms
 
class curso_formulario (forms.Form):
    nombre= forms.CharField(max_length= 50)
    comision= forms.IntegerField()
