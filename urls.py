"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'load_all/', 
        views.load_all, 
        name='report__load_all'
    ),
]