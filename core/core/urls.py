"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('testai/', include('testai.urls')),
]
