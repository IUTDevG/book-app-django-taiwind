from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    id = models.CharField(primary_key=True,max_length=36,default=uuid.uuid4,editable=False)
    email = models.EmailField(max_length=100,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
