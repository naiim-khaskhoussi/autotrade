# Generated by Django 3.1.5 on 2021-01-10 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210110_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
