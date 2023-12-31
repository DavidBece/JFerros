# Generated by Django 4.2.6 on 2023-11-01 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_apellido_alter_usuario_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='municipio',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message='Este campo solo permite letras.')]),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='telefono',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d+$ ', message='Este campo solo permite números.')], verbose_name='Teléfono'),
        ),
    ]
