# Generated by Django 5.1.3 on 2025-04-01 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='fecha_Creacion',
            new_name='fecha_creacion',
        ),
    ]
