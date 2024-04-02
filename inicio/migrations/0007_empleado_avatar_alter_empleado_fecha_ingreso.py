# Generated by Django 5.0.2 on 2024-03-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_empleado_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_empleados'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(),
        ),
    ]
