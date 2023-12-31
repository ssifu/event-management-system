# Generated by Django 4.2.7 on 2023-11-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0007_remove_event_available_slots_event_registered_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='registered_events',
            field=models.ManyToManyField(through='event_management.UserEventRegistration', to='event_management.event'),
        ),
    ]
