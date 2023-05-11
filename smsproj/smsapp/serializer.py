from rest_framework import serializers
from .models import sms


class smsserializer(serializers.ModelSerializer):
    class Meta:
        model = sms
        fields = '__all__'
