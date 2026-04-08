from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from .serializers import OrderItemSerializer, OrderSerializer
from .models import Order, OrderItem
from django.conf import settings
User = settings.AUTH_USER_MODEL
