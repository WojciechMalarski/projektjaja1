# Generated by Django 4.0.4 on 2022-06-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ilosc1A', models.IntegerField(default=0)),
                ('Cena1A', models.IntegerField(default=160)),
                ('Suma1A', models.IntegerField(default=0)),
            ],
        ),
    ]
