from rest_framework import serializers
from django.db.models import Avg

from .models import Category, Item, Rating



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['ratings'] = instance.rating.aggregate(Avg('rate'))['rate__avg']
    #     return representation



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def validate(self, attrs):
        user = self.context.get('request').user
        item = self.context.get('item')
        rate = Rating.objects.filter(user=user, item=item).exists()
        if rate:
            raise serializers.ValidationError({'message': 'Оценка уже стоит'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
    