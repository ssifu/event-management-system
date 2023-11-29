from rest_framework import serializers
from .models import Event, UserEventRegistration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class UserEventRegistrationSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = UserEventRegistration
        fields = '__all__'
