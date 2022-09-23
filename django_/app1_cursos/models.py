from django.db import models

class Posteo (models.Model):
    ciudad=models.CharField(max_length=60)
    pais=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenes', null=True)
    fecha=models.DateField()
    autor=models.CharField(max_length=250)
    descripcion= models.CharField(max_length=250)
