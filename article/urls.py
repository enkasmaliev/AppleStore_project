from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemViewSet, CommentViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet, 'categories')
router.register('item', ItemViewSet, 'items')
router.register('comment', CommentViewSet, 'comments')

urlpatterns = router.urls