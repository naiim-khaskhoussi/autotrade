# Generated by Django 3.1.5 on 2021-01-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_brand_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='kilometers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.fueltype'),
        ),
    ]
