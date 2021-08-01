from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    # the next two lines enable log in with email instead of a username
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
