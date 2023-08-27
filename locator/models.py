from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=50)
    message = models.TextField(default="")

    def __str__(self):
        return self.name


class IpAddress(models.Model):
    address = models.CharField(default="", max_length=500)

    def __str__(self):
        return self.address