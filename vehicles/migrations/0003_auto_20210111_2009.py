# Generated by Django 3.1.5 on 2021-01-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(default='photos/Grande_punto_5tuerer.jpeg', upload_to='photos/'),
        ),
    ]
