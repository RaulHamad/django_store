from Book_store.models.book.editor import *
from django.db import models



class Editor(models.Model):

    name = models.CharField(null=False, blank=False,max_length=100)


    def __str__(self) -> str:
        return self.name