"""
mandrill_webhooks URL Configuration
"""
from django.contrib import admin
from django.urls import path

from events.views import Home, Webhook

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("webhook/", Webhook.as_view(), name="webhook"),
]
