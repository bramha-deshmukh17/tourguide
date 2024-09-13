# Generated by Django 5.0.2 on 2024-05-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0029_booking_feedback_tourguide_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='comment',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='booking',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
