from django.contrib import admin
from .models.book.book import *
from .models.book.author import *
from .models.book.editor import *
from .models.book.rating import *
from .models.profile.profile import *
from .models.profile.shopping import *
from .models.category.category import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Editor)
admin.site.register(Rating)
admin.site.register(Profile)
admin.site.register(Shopping)
admin.site.register(Category)
