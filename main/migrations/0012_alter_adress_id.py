# Generated by Django 4.1.2 on 2022-12-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_kupac_adresa_id_kupac_kupac_adresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
