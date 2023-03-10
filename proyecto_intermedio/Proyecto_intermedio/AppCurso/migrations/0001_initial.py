# Generated by Django 4.1.7 on 2023-03-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('fecha_de_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alumno', models.CharField(max_length=40)),
                ('nombre_entregable', models.CharField(max_length=30)),
                ('curso', models.CharField(max_length=30)),
                ('fecha_de_entrega', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=30)),
                ('rol', models.CharField(max_length=15)),
                ('profesion', models.CharField(max_length=30)),
            ],
        ),
    ]
