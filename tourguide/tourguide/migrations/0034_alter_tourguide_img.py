# Generated by Django 5.0.2 on 2024-05-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0033_alter_tourguide_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourguide',
            name='img',
            field=models.ImageField(default='guide/default_User_o.png', upload_to='guide'),
        ),
    ]
