from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Cart.objects.filter(user=self.request.user)
    
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)
