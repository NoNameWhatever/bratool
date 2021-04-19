from django.urls import path, include

from users.views import apiListView

urlpatterns = [
    path('list/', apiListView.as_view(), name='api_list'),   
]