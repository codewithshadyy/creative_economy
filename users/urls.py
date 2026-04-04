
from .views import RegisterView
from django.urls import path
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView


    
)

urlpatterns = [

    path("register/", RegisterView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="signin"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh")
]
