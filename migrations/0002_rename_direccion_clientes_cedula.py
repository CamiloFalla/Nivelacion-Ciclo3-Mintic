# Generated by Django 4.1 on 2022-10-14 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionServicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='direccion',
            new_name='cedula',
        ),
    ]
