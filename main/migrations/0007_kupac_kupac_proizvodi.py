# Generated by Django 4.1.2 on 2022-12-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_proizvod_proizvod_vrstap'),
    ]

    operations = [
        migrations.AddField(
            model_name='kupac',
            name='kupac_proizvodi',
            field=models.ManyToManyField(to='main.proizvod'),
        ),
    ]
