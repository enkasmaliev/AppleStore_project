from django.contrib import admin

from .models import Category, Item, Rating

admin.site.register([Category, Item, Rating])
