# Generated by Django 2.2.2 on 2019-08-05 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190805_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='team_name',
            new_name='name',
        ),
    ]
