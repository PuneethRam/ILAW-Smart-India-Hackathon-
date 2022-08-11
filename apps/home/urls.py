# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('adddb', views.addCasetoDB, name='adddb'),
    path('add', views.addTodo, name='add'),
    path('sec', views.sec, name='sec'),
    path('trans', views.translate, name='trans'),

   
    #path('analysis/',views.analysis),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
]
