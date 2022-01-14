from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Donor(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
