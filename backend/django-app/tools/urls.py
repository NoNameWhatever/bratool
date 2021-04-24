from django.urls import path, include

from rest_framework.routers import DefaultRouter

from tools import views

router = DefaultRouter()
router.register('tools-viewset', views.ToolsViewset, basename='tools-viewset')
router.register('tool', views.ToolViewSet)


urlpatterns = [
    path('list/', views.ToolApiView.as_view(), name='api_list'),
    path('', include(router.urls))
]