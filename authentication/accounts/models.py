from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=100, unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    profile_img = models.ImageField(upload_to="profile")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


