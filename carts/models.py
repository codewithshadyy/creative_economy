from django.db import models
from django.conf import settings
from products.models import Product
User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart-{self.user}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ["cart", "product"]

    def __str__(self):
        return f"{self.product.name} ({self.product})" 

    # def get_or_create_cart(self):
    #     cart, created = Cart.objects.get_or_create(user=User)
    #     return cart       