from django.urls import path
from Book_store.views.homeView import home


urlpatterns = [
    
    path("", home),
]