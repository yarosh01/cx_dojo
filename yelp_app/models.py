from django.db import models
from django.utils import timezone


class Cafe(models.Model):

    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    categories = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    rating_google = models.CharField(max_length=250)

    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
