from .views import CartViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cart", CartViewSet)

urlpatterns = router.urls


