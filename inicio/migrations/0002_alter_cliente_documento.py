# Generated by Django 5.0.2 on 2024-03-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.IntegerField(),
        ),
    ]
