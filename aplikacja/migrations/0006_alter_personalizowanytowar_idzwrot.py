# Generated by Django 4.0.5 on 2022-06-18 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0005_klient_idadres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalizowanytowar',
            name='idZwrot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplikacja.zwrot'),
        ),
    ]
