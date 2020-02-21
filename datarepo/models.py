from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    email = models.EmailField()
    dob = models.DateField()
