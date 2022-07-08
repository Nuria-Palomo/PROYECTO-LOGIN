# Generated by Django 4.0.6 on 2022-07-04 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('dni', models.CharField(max_length=9)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=25)),
                ('fNacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=25)),
                ('comentarios', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=25)),
                ('materia', models.ManyToManyField(to='codersapp.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(blank=True, null=True)),
                ('comentario', models.TextField(max_length=100)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codersapp.alumno')),
                ('materia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codersapp.materia')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='materia',
            field=models.ManyToManyField(to='codersapp.materia'),
        ),
    ]
