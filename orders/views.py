from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OrderItemSerializer, OrderSerializer
from .models import Order, OrderItem
from carts.models import Cart
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend  
from rest_framework import filters





from django.conf import settings
User = settings.AUTH_USER_MODEL

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
    

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

   
    @action(detail=False, methods=['post'])
    @transaction.atomic
    def checkout(self, request):
        cart = Cart.objects.get(user=request.user)

        if not cart.items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        order = Order.objects.create(user=request.user, total_price=0)

        total = 0
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            total += item.product.price * item.quantity

        order.total_price = total
        order.save()

        cart.items.all().delete()

        return Response({"message": "Order placed successfully"})

 
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()

        if order.status != "pending":
            return Response({"error": "Cannot cancel this order"}, status=400)

        order.status = "cancelled"
        order.save()

        return Response({"message": "Order cancelled"})

   
    @action(detail=True, methods=['patch'])
    def status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get("status")

        order.status = new_status
        order.save()

        return Response({"message": "Status updated"})