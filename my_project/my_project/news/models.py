from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Editorial(models.Model):
    Heading = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)

    def __str__(self):
        return self.Heading
