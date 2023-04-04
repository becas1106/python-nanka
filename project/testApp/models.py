from django.db import models

class Test(models.Model):
    id = models.IntegerField(primary_key=True)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

