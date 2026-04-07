from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
   
class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return CartItem.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def add_item(self,request, pk=None):
        cart = self.get_object()
        product_id = request.data.get("product")
        quantity = int(request.data.get("quanity", ))


        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            defaults={'quantity': quantity}

        )  


        if not created:
            item.quantity += quantity
            item.save()

        return Response({"message":"Added  to Cart"}, status=status.HTTP_201_CREATED)          
                 





       