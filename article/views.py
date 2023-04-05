from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Item, Rating, Comment
from .serializers import CategorySerializer, ItemSerializer, RatingSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthor


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # filterset_fields = ['categories', 'status']
    search_fields = ['name', 'categories__name']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

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

    



class CommentViewSet(ItemViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthor, ]
        return super().get_permissions()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context