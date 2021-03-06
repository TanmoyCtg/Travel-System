from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name="hotels"),
    path('<int:hotels_id>', views.hotels, name='hotel'),
    path('search', views.search, name='search'),
]
