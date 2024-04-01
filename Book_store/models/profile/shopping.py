from django.db import models
from Book_store.models.profile.profile import *
from Book_store.models.book.book import *

from django.contrib.auth.models import User


class Shopping (models.Model):

    user_id = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE )
    product_id = models.ForeignKey(Book,null=False,blank=False,on_delete=models.CASCADE)
    date_buy = models.DateTimeField(null=True,auto_now_add=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user_id