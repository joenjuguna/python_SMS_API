from django.db import models

# Create your models here.
class sms(models.Model):
    title = models.CharField(max_length = 100)
    sender = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.title