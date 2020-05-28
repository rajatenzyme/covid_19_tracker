from django.db import models

# Create your models here.
from django_countries.fields import CountryField

class Foo(models.Model):
    country = CountryField()

