# Generated by Django 5.0.2 on 2024-03-12 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0016_tourguide_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('pickup', models.CharField(max_length=50)),
                ('venu', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourguide.customer')),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourguide.tourguide')),
            ],
        ),
    ]
