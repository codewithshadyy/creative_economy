from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import actions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OrderItemSerializer, OrderSerializer
from .models import Order, OrderItem
from carts.models import Cart

from django.conf import settings
User = settings.AUTH_USER_MODEL

class OrderViewset(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]
    @actions(detail=False, methods=['post'])
    def checkout(self, request):
        cart = Cart.objects.get(user=request.user)

        if not cart.items.exists():
            return Response({'message':"sorry the cart is empty"})
        order = Order.objects.create(user=request.user, tota_price=0)

        total=0

        for item in cart.items.all():
            OrderItem.objects.create(
                order = order,
                product =item.product,
                quantity = item.quantity,
                price = item.price
            )
          
        total += item.quantity * item.price
        order.total_price = total
        order.save()
        cart.items.all().delete()

        return Response({'message':'order placed successfully'})

