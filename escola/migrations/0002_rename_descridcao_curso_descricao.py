# Generated by Django 4.0.1 on 2022-01-19 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='descridcao',
            new_name='descricao',
        ),
    ]
