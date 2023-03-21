import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


@method_decorator(csrf_exempt, name="dispatch")
class Webhook(View):
    async def head(self, request, *args, **kwargs):
        return HttpResponse(status=200)

    async def post(self, request, *args, **kwargs):
        try:
            if "mandrill_events" in request.POST:
                events = json.loads(request.POST["mandrill_events"])
                for event in events:
                    event_type = event.get('event')
                    msg_id = event.get('msg', {}).get('_id')
                    subject = event.get('msg', {}).get('subject')
                    email = event.get('msg', {}).get('email')
                    message = event.get('msg', {})
                    if event_type and msg_id:
                        # Set message to Redis cache
                        cache.set(msg_id, message)
            else:
                return HttpResponse("Empty events", status=400)
            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)
