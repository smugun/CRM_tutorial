from django.db import models

# Create your models here.


class FarmRecords(models.Model):
    farm_items = models.CharField(max_length=50)
    quantity = models.IntegerField(blank=False)
    units = models.CharField(max_length=50)
    period = models.DateField(max_length=20)
    cost = models.IntegerField(blank=False)

    def __str__(self):
        return self.farm_items


class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class RegistrationForm:
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username
