# Generated by Django 2.2.3 on 2023-07-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_property_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='flat_type',
            field=models.CharField(choices=[('1', '1BHK'), ('2', '2BHK'), ('3', '3BHK')], max_length=20),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='possession',
            field=models.CharField(choices=[('1', 'ready to move'), ('2', 'work on progress')], max_length=20),
        ),
        migrations.AlterField(
            model_name='property_details',
            name='price_range',
            field=models.CharField(choices=[('1', '$5000'), ('2', '$15,000'), ('3', '$25,000'), ('4', '$40,000'), ('5', '$50,000')], max_length=50),
        ),
    ]
