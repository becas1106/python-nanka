from django.urls import path
from . import views

app_name = 'testApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.top, name='top'),
    path('register', views.register, name='register'),
]
