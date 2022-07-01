# Generated by Django 4.0.4 on 2022-06-02 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombrecompleto', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='nombre')),
                ('numero', models.CharField(max_length=20, verbose_name='numero')),
                ('domicilio', models.CharField(max_length=50, null=True, verbose_name='Domicilio')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('sexo', models.BooleanField(default=True, max_length=1, verbose_name='sexo')),
                ('color', models.CharField(max_length=50, verbose_name='color')),
                ('esterilizado', models.BooleanField(default=True, max_length=2, verbose_name='Esterilizado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.cliente')),
            ],
        ),
    ]
