from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    last_logout_time =models.DateTimeField(null=True, blank= True)
    forget_password = models.CharField(max_length=255, blank=True, null=True)

    objects= UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
