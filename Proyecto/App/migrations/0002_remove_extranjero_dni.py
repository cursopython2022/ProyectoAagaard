# Generated by Django 4.0.4 on 2022-06-14 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extranjero',
            name='dni',
        ),
    ]
