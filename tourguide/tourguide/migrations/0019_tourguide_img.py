# Generated by Django 5.0.2 on 2024-03-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0018_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourguide',
            name='img',
            field=models.ImageField(default='f', upload_to='guide'),
        ),
    ]
