
from Book_store.models.book.book import *
from Book_store.models.category.category import *
from django.db import models


class Book(models.Model):

    title = models.CharField(null=False, max_length=150)
    summary = models.TextField(null = True, blank = True)
    editor = models.ForeignKey("Editor",null=False, on_delete=models.CASCADE,related_name='editor')
    author = models.ForeignKey("Author",null =False,on_delete=models.CASCADE,related_name='author')
    isbn = models.IntegerField(null=True)
    no_pages = models.IntegerField(null=True, blank = True)
    price = models.DecimalField(decimal_places=2, null = False,max_digits = 10)
    release_date_of = models.DateField(auto_now=False, auto_now_add=False)
    download = models.FileField(upload_to="%Y/%m/%d",null=True,blank=True)
    quantity = models.IntegerField(default = 10)
    status = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True,related_name='Category')



    def __str__(self):
        return self.title

 