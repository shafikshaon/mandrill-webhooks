"""
mandrill_webhooks URL Configuration
"""
from django.contrib import admin
from django.urls import path

from events.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
]
