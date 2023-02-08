from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class User(AbstractUser):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    OTP = models.CharField(max_length=6, blank=True, null=True)
    authenticated = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    account_creation_time = models.DateTimeField(auto_now_add=True)
    account_status = models.CharField(max_length=20, default='active')

    objects= UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
