# Generated by Django 4.1.2 on 2022-12-21 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_proizvod_proizvod_vrstap'),
    ]

    operations = [
        migrations.AddField(
            model_name='proizvod',
            name='proizvod_vrstaP',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.vrstaproizvoda'),
            preserve_default=False,
        ),
    ]
