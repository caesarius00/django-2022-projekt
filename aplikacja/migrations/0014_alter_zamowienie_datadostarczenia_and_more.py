# Generated by Django 4.0.5 on 2022-06-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0013_alter_zamowienie_datadostarczenia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamowienie',
            name='dataDostarczenia',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='dataWyslania',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zwrot',
            name='dataOtrzymania',
            field=models.DateField(blank=True, null=True),
        ),
    ]