from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='rango-index'),
    path('about/', views.about, name='rango-about')
]