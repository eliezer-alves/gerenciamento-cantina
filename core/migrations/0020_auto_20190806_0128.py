# Generated by Django 2.2.2 on 2019-08-06 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190806_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='date_p',
            new_name='date',
        ),
    ]
