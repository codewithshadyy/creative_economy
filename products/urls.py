from rest_framework.routers import DefaultRouter
from .views import ProductView, CategoryViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductView)

urlpatterns = router.urls