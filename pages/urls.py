"""Defines URL patterns for pages."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('violations', views.violations, name='violations'),
    path('purifier', views.purifier, name='purifier'),
    path('events', views.events, name='events'),

]