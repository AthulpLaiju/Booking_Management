from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)




