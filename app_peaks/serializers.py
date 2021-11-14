from django.db.models import fields
from .models import UserPeak
from rest_framework import serializers

class UserPeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPeak
        fields = '__all__'