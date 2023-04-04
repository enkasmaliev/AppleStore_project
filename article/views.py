from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Item, Rating
from .serializers import CategorySerializer, ItemSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
    

    def get_serializer_class(self):
        if self.action == 'rate_item':
            return RatingSerializer
        return super().get_serializer_class()
    
    @action(methods=['POST'], detail=True, url_path='rate')
    def rate_item(self, request):
        item = self.get_object()
        serializer = RatingSerializer(data=request.data, context={'request': request, 'item': item})
        serializer.is_valid(raise_exception=True)
        serializer.save(item=item)
        return Response(serializer.data)
