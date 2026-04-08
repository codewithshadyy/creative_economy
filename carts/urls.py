from .views import CartViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("cart", CartViewSet)
# router.register("cart-items", CartItemViewset)

urlpatterns = router.urls


