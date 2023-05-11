from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import sms
from .serializer import smsserializer

# Create your views here.
class smsAPI(ModelViewSet):
    queryset = sms.objects.all()
    serializer_class = smsserializer
