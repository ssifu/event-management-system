from django.contrib import admin

from .models import Users, Event, UserEventRegistration

# Register your models here.
admin.site.register(Users)
admin.site.register(Event)
admin.site.register(UserEventRegistration)
