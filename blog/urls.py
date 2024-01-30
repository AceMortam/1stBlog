# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:21:55 2024

@author: guill
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]