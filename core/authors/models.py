from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=34)
    def __str__(self):
        return self.name