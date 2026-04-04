from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('BUYER', 'Buyer'),
        ('SELLER', 'Seller')
    )
    role = models.CharField(choices=ROLE_CHOICES, default='BUYER')
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        self.username


