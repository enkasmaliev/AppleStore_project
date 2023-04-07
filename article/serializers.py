from rest_framework import serializers
from .models import Category, Item, Rating, Comment, ItemCollection
from django.db.models import Avg



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        user_id = self.context.get('request').user.id
        validated_data['user_id'] = user_id
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['categories'] = [category.name for category in instance.categories.all()]
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        # representation['rating'] = instance.rating.aggregate(Avg('rate'))['rate__avg']
        return representation



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
    

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'user', 'item', 'text', 'created_at', 'updated_at')
        

class ItemCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCollection
        fields = ('id', 'text', 'items', 'created_at', 'updated_at',)


