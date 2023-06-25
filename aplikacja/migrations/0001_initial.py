# Generated by Django 4.0.5 on 2022-06-18 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('Nick', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Imie', models.CharField(max_length=50)),
                ('Nazwisko', models.CharField(max_length=50)),
                ('nrTelefonu', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Zwrot',
            fields=[
                ('idZwrot', models.IntegerField(primary_key=True, serialize=False)),
                ('Powod', models.CharField(max_length=256)),
                ('DataWyslania', models.DateField()),
                ('DataOtrzymania', models.DateField()),
                ('CzyZwroconoPieniadze', models.BooleanField()),
                ('Nick', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aplikacja.klient')),
            ],
        ),
        migrations.CreateModel(
            name='Opinia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gwiazdki', models.IntegerField()),
                ('Komentarz', models.CharField(max_length=256)),
                ('Nick', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aplikacja.klient')),
            ],
        ),
    ]