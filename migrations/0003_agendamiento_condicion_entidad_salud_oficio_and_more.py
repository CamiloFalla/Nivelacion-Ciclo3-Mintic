# Generated by Django 4.1 on 2022-10-15 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionServicios', '0002_rename_direccion_clientes_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamiento',
            fields=[
                ('idAgendamiento', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('horario_a', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicativo_c', models.CharField(max_length=45)),
                ('condicion_c', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad_salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_es', models.CharField(max_length=45)),
                ('valor_es', models.CharField(max_length=45)),
                ('nit', models.CharField(max_length=45)),
                ('sector_productivo', models.CharField(max_length=45)),
                ('fecha_creacion', models.DateTimeField()),
                ('ciudad', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oficio_o', models.CharField(max_length=45)),
                ('indicativo_o', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_t', models.CharField(max_length=45)),
                ('fecha_t', models.CharField(max_length=45)),
                ('descripcion_t', models.CharField(max_length=45)),
                ('Entidad_salud_idEntidad_salud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.entidad_salud')),
                ('Oficio_idOficio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.oficio')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_u', models.CharField(max_length=45)),
                ('apellidos_u', models.CharField(max_length=45)),
                ('documento_u', models.CharField(max_length=45, unique=True)),
                ('email_u', models.EmailField(max_length=254, unique=True)),
                ('telefono_u', models.CharField(max_length=45)),
                ('direccion_u', models.CharField(max_length=45)),
                ('nombre_r', models.CharField(max_length=45)),
                ('telefono_r', models.CharField(max_length=45)),
                ('parentesco_r', models.CharField(max_length=45)),
                ('documento_r', models.CharField(max_length=45)),
                ('usuario_u', models.CharField(max_length=45, unique=True)),
                ('password_u', models.CharField(max_length=45)),
                ('Condicion_idCondicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.condicion')),
                ('Entidad_salud_idEntidad_salud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.entidad_salud')),
                ('Transaccion_idTransaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.transaccion')),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('idEmpleados', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombres_e', models.CharField(max_length=45)),
                ('apellidos_e', models.CharField(max_length=45)),
                ('documento_e', models.CharField(max_length=45, unique=True)),
                ('email_e', models.EmailField(max_length=254, unique=True)),
                ('telefono_e', models.CharField(max_length=45)),
                ('direccion_e', models.CharField(max_length=45)),
                ('tFecha_creacion', models.CharField(max_length=45)),
                ('Agendamiento_ideAgendamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.agendamiento')),
                ('Condicion_idCondicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.condicion')),
                ('Oficio_idOficio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.oficio')),
            ],
        ),
        migrations.AddField(
            model_name='agendamiento',
            name='Transaccion_idTransaccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.transaccion'),
        ),
        migrations.AddField(
            model_name='agendamiento',
            name='Usuarios_idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionServicios.usuarios'),
        ),
    ]
