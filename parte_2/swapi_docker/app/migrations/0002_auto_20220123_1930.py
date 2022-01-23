# Generated by Django 2.2.13 on 2022-01-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('blue', 'BLUE'), ('white', 'WHITE'), ('purple', 'PURPLE'), ('unknown', 'UNKNOWN'), ('brown', 'BROWN'), ('red', 'RED'), ('yellow', 'YELLOW'), ('black', 'BLACK'), ('green', 'GREEN')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('white', 'WHITE'), ('none', 'NONE'), ('bald', 'BALD'), ('blonde', 'BLONDE'), ('brown', 'BROWN'), ('red', 'RED'), ('black', 'BLACK')], max_length=32),
        ),
    ]
