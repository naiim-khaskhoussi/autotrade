# Generated by Django 3.1.5 on 2021-01-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(default='file1', upload_to=''),
            preserve_default=False,
        ),
    ]
