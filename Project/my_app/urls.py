# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:05:25 2021

@author: Piyush
"""

from django.urls import path, include
from . import views

urlpatterns = [path('', views.index, name='index')]