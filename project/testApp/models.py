from django.db import models
from django.contrib.auth.models import User
import uuid

class Test(models.Model):
    id = models.IntegerField(primary_key=True)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

