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
    path(
        'send_one/', 
        views.send_one, 
        name='report__send_one'
    ),
    path(
        'send_multiple/', 
        views.send_multiple, 
        name='report__send_multiple'
    ),
]