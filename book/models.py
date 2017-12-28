from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=150,blank=True, null=True)
    author = models.CharField(max_length=150,blank=True, null=True)
    data_published = models.DateField(blank=True, null=True)
    number_of_page = models.IntegerField(blank=True, null=True)
    type_of_book = models.CharField(max_length=35,blank=True, null=True)

    class Meta:
        db_table = 'book'
