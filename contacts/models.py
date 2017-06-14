from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
from django_countries.fields import CountryField

from contacts.constants import GenderSource

GENDER_CHOICES = (
    (GenderSource.Male, 'M',),
    (GenderSource.Female, 'F',),
)

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    middle_name = models.CharField(max_length=90, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True)
    mobile_number = models.CharField(max_length=32, null=True)
    email = models.CharField(max_length=128, null=True)


class Location(models.Model):
    person = models.ForeignKey(Person, null=True)
    raw = models.CharField(max_length=200, null=True, help_text='address line 1')
    unit_no = models.CharField(max_length=6, null=True)
    street_number = models.CharField(max_length=32, null=True)
    street_name = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64, null=True)
    suburb = models.CharField(max_length=64, null=True)
    state_province_code = models.CharField(max_length=32, null=True)
    postal_code = models.CharField(max_length=32, null=True)
    country = CountryField(null=True)
