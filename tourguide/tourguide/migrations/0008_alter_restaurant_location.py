# Generated by Django 5.0.2 on 2024-03-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0007_alter_hotel_location_alter_place_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.URLField(max_length=500),
        ),
    ]
