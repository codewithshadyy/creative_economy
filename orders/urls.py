from .views import OrderViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"order", OrderViewSet)

urlpatterns =router.urls
