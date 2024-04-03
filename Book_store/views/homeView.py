from django.shortcuts import render
from Book_store.models.category.category import Category


def home(request):
    category = Category.objects.all()
    len_category = len(category)
    context = {"category": category, 'len_category': len_category}



    return render(request,"home.html", context=context)