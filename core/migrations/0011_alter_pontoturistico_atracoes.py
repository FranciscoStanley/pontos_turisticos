# Generated by Django 3.2.7 on 2021-11-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_alter_atracao_fotos'),
        ('core', '0010_auto_20211111_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(blank=True, null=True, to='atracoes.Atracao'),
        ),
    ]