# Generated by Django 4.2.7 on 2023-11-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0005_usereventregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='available_slots',
            field=models.IntegerField(default=10),
        ),
    ]
