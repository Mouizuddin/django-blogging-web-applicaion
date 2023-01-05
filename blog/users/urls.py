from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('register/' , views.user_reg , name='user_reg'),

]
