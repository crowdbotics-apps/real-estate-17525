from django.conf import settings
from django.db import models


class Registered_agent(models.Model):
    "Generated Model"
    name = models.CharField(max_length=98,)
    employee_ref_num = models.PositiveIntegerField()
    address_1 = models.CharField(max_length=150,)


# Create your models here.
