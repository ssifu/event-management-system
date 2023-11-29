# from django.contrib.auth.models import User
from enum import unique
from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location_name = models.CharField(max_length=100, blank=True, null=True)
    max_slots = models.IntegerField()
    created_at = models.DateTimeField()

    def formatted_datetime(self):
        return {
            "date": self.date.strftime("%d"),
            "month": self.date.strftime("%b").upper(),
            "time": self.time.strftime("%I:%M%p"),
        }

    def __str__(self):
        return self.title


class UserEventRegistration(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
