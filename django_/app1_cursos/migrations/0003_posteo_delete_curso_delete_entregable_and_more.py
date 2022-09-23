# Generated by Django 4.1 on 2022-09-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_cursos', '0002_entregable_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha', models.DateField()),
                ('autor', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
