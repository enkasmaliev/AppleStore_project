from django.contrib import admin

from .models import Category, Item, Rating, Comment


admin.site.register([Category, Item, Rating, Comment])
