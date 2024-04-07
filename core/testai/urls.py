from django.urls import path, include
from rest_framework.routers import DefaultRouter

from testai import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'testai', views.TestViewSet, basename='testai')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]