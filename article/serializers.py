from rest_framework import serializers
from .models import Category, Item



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
class ItemSerializer(serializers.ModelField):
    class Meta:
        model = Item
        fields = '__all__'
        