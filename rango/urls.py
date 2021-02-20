from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='rango-index'),
    path('about/', views.about, name='rango-about'),
    path('category/<slug:category_name_slug>/', views.show_category, name="show_category")
]