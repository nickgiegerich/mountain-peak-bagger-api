from django.db import models
from app_user.models import CustomUser

# Create your models here.
class UserPeak(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    location_descr = models.CharField(max_length=150, null=True)
    latitude = models.FloatField(max_length=20, default=0)
    longitude = models.FloatField(max_length=20, default=0)
    summit_date = models.DateField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
