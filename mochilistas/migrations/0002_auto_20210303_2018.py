# Generated by Django 3.1.7 on 2021-03-03 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mochilistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Escolas',
            name='tempo_de_servico',
            field=models.IntegerField(default=0),
        ),
    ]
