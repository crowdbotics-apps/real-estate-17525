from django.conf import settings
from django.db import models


class Company(models.Model):
    "Generated Model"
    company_name = models.CharField(max_length=200,)
    address_1 = models.CharField(max_length=200, null=True, blank=True,)
    address_2 = models.CharField(max_length=200, null=True, blank=True,)
    city = models.CharField(max_length=100, null=True, blank=True,)
    state = models.CharField(max_length=100, null=True, blank=True,)
    zip_code = models.PositiveSmallIntegerField(null=True, blank=True,)


# Create your models here.
