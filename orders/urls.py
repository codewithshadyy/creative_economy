from .views import OrderViewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register("order", OrderViewset)

urlpatterns =router.urls
