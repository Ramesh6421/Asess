from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
# Create your models here.


class RiderModel(models.Model):
    CHOICES = (('bus','BUS'),('car','CAR'),('train','TRAIN'))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    From = models.CharField(max_length = 50)
    To = models.CharField(max_length = 50)
    DateTime = models.DateTimeField(default = datetime.now())
    Travel_Medium = models.CharField(max_length = 20, choices = CHOICES)
    Asset_Quantity = models.IntegerField(default = 0)


class RequesterModel(models.Model):
    Type_CHOICES = (('laptop','LAPTOP'),('travel_bag','TRAVEL_BAG'),('package','PACKAGE'))
    Sensitivity_CHOICES = (('highly_sensitive','HIGHLY_SENSITIVE'),('sensitive','SENSITIVE'),('normal','NORMAL'))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    From = models.CharField(max_length = 50)
    To = models.CharField(max_length = 50)
    DateTime = models.DateTimeField(default = datetime.now())
    No_Of_Assets = models.IntegerField(default=0)
    Asset_Type = models.CharField(max_length = 20, choices = Type_CHOICES)
    Asset_Sensitivity = models.CharField(max_length = 20, choices = Sensitivity_CHOICES)
    Whom_To_Deliver = models.CharField(max_length = 50)