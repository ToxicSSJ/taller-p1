# Generated by Django 3.0.6 on 2020-05-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminosity', '0002_auto_20200513_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luminosity',
            name='value',
            field=models.CharField(max_length=25, verbose_name='tipo_de_terreno'),
        ),
    ]
