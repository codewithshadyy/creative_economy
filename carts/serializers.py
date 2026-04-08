from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_id = serializers.IntegerField(source="product.id", read_only=True)
    price = serializers.DecimalField(source="product.price", decimal_places=2, max_digits=10, read_only=True)

    class Meta:
        model = CartItem
        fields = ["id",  "product_id", "product_name", "quantity", "price"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    

    class Meta:
        model = Cart
        fields = ["id", "user_id", "items"]