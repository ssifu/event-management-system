from django.contrib import admin

from .models import Users, Event

# Register your models here.
admin.site.register(Users)
admin.site.register(Event)
