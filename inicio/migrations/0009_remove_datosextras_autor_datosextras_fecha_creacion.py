# Generated by Django 5.0.2 on 2024-03-29 03:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_datosextras_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosextras',
            name='autor',
        ),
        migrations.AddField(
            model_name='datosextras',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
