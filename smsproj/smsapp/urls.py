from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import smsAPI
router = DefaultRouter()
router.register(r'sms',smsAPI)

urlpatterns = [
    path('', include(router.urls)),
]
