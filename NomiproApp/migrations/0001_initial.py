# Generated by Django 3.0.6 on 2020-06-04 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('estado', models.CharField(max_length=15)),
                ('valorCargo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ControlPagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorHorasExtras', models.FloatField()),
                ('valorParafiscal', models.FloatField()),
                ('mes', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('tipoDocumento', models.CharField(max_length=45)),
                ('numeroDocumento', models.CharField(max_length=45)),
                ('idCargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Cargos')),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoHorario', models.CharField(max_length=20)),
                ('hora', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HorasExtras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('valor', models.FloatField()),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Parafiscales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('valor', models.FloatField()),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vinculaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ParafiscalesxEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=20)),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Empleados')),
                ('idParafiscales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Parafiscales')),
            ],
        ),
        migrations.CreateModel(
            name='Nominas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=15)),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('idCargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Cargos')),
                ('idControlPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.ControlPagos')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Empleados')),
            ],
        ),
        migrations.CreateModel(
            name='HExtraxEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroHoras', models.IntegerField()),
                ('mes', models.CharField(max_length=15)),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Empleados')),
                ('idHExtras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.HorasExtras')),
            ],
        ),
        migrations.AddField(
            model_name='empleados',
            name='idHorario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Horarios'),
        ),
        migrations.AddField(
            model_name='empleados',
            name='idVinculacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Vinculaciones'),
        ),
        migrations.AddField(
            model_name='controlpagos',
            name='idEmpleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NomiproApp.Empleados'),
        ),
    ]