from django.shortcuts import render
from Book_store.models.category.category import Category


def home(request):
    category = Category.objects.all()
    context = {"category": category}



    return render(request,"home.html", context=context)