from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from products.models import Product




class CartViewSet(viewsets.ViewSet):
    queryset = Cart.objects.all()
    
    permission_classes = [IsAuthenticated]
    

    def get_cart(self, user):
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart

    def list(self, request):
        cart = self.get_cart(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add(self, request):
        cart = self.get_cart(request.user)

        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        
        if not product_id:
            return Response({"error": "Product is required"}, status=400)

        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                return Response({"error": "Quantity must be > 0"}, status=400)
        except:
            return Response({"error": "Invalid quantity"}, status=400)

        
       
        product = Product.objects.filter(id=product_id).first()

        if not product:
            return Response({"error": "Product not found"}, status=404)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,  
            defaults={'quantity': quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

        return Response({"message": "Item added to cart"})

