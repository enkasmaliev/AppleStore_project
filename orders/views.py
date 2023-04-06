from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

