from django.urls import path, include
from rest_framework.routers import DefaultRouter

from testai import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'tests', views.TestViewSet, basename='tests')
router.register(r'testcase', views.TestCaseViewSet, basename='testcase')
router.register(r'teststep', views.TestStepViewSet, basename='teststep')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]