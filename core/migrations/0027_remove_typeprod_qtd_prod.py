# Generated by Django 2.2.2 on 2019-08-15 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_typeprod_qtd_prod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeprod',
            name='qtd_prod',
        ),
    ]
