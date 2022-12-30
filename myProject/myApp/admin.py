from django.contrib import admin
from . models import RiderModel,RequesterModel

# Register your models here.

admin.site.register(RiderModel)

admin.site.register(RequesterModel)