from Book_store.models.book import *
from django.db import models

class Category(models.Model):

    name= models.CharField(max_length=32,null=False,blank=False)
    category = models.ImageField(null=True,blank=True)
    about = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.name