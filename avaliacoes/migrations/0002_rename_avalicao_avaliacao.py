# Generated by Django 3.2.7 on 2021-10-10 22:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_alter_pontoturistico_enderecos'),
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avalicao',
            new_name='Avaliacao',
        ),
    ]
