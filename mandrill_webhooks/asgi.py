"""
ASGI config for mandrill_webhooks project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

from events.consumers import MandrillConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mandrill_webhooks.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(
            [
                path("ws/mandrill/", MandrillConsumer.as_asgi()),
            ]
        ),
    }
)
