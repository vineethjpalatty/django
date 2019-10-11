from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)
    info = models.CharField(max_length=60, null=True, blank=True, )
    def __str__(self):
        return self.name

