from Book_store.models.book.book import *
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

   user = models.OneToOneField(User,on_delete=models.CASCADE)
   email = models.EmailField(unique = True)
   image = models.ImageField(upload_to="profile/%Y/%m/%d",null=True,blank=True)
   address = models.CharField(max_length=200,null=True,blank=True)
   create_at = models.DateField(auto_now=True)
   

   def __str__(self) -> str:
      return self.user
