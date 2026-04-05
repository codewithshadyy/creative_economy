
from .views import (
    RegisterView,
    PasswordResetConfirmView,
    PasswordResetView
                    )
from django.urls import path
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView


    
)

urlpatterns = [

    path("register/", RegisterView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="signin"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("password-reset/", PasswordResetView.as_view(), name="password-reset"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="confirm-reset"),
]
