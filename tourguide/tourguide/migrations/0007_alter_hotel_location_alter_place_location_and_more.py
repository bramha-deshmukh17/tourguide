# Generated by Django 5.0.2 on 2024-03-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0006_alter_hotel_img_alter_place_img_alter_restaurant_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]
