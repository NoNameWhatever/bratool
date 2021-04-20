from django.urls import path
from tools import views



urlpatterns = [
    path('list/', views.ToolApiView.as_view(), name='api_list'),   
]