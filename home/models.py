from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pages=models.IntegerField( null= True ,blank=True)

    class Meta:
        verbose_name_plural='Books'

    def __str__(self):
        return name
