from django.contrib import admin
from .models import Test
admin.site.register(Test)
from .models import User
admin.site.register(User)
