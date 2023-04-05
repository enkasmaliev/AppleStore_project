from rest_framework import serializers
from .models import Category, Item, Rating, Comment



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



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
        read_only_fields = ['item']




