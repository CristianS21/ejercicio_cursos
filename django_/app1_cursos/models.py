from django.db import models

class Posteo (models.Model):
    imagen=models.ImageField(upload_to='imagenes', null=True)
    fecha=models.DateField()
    autor=models.CharField(max_length=250)
    descripcion= models.CharField(max_length=250)
