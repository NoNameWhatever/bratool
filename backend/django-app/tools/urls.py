from django.urls import path, include
from . import views



urlpatterns = [
    path('list/', views.apiListView, name='api_list'),   
]