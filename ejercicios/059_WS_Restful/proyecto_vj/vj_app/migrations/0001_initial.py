# Generated by Django 4.0.3 on 2022-03-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('plataforma', models.CharField(max_length=50)),
                ('anyo', models.IntegerField()),
            ],
        ),
    ]