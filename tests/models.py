from django.db import models
from django.contrib.postgres.fields import HStoreField

class DataBag(models.Model):
    name = models.CharField(max_length=32)
    data = HStoreField()
