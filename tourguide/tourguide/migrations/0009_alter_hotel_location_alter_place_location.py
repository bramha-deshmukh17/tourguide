# Generated by Django 5.0.2 on 2024-03-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0008_alter_restaurant_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.URLField(max_length=500),
        ),
    ]
