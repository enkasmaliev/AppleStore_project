from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet, 'categories')
router.register('item', ItemViewSet, 'items')


urlpatterns = router.urls