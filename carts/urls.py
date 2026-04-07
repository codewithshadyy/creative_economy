from .views import CartViewSet, CartItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cart", CartViewSet)
router.register("items", CartItemViewSet)

urlpatterns = router.urls


