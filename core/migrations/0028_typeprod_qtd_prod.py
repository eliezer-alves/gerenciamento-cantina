# Generated by Django 2.2.2 on 2019-08-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_remove_typeprod_qtd_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeprod',
            name='qtd_prod',
            field=models.IntegerField(default=0),
        ),
    ]
