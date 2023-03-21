import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


@method_decorator(csrf_exempt, name="dispatch")
class Webhook(View):
    def head(self, request, *args, **kwargs):
        return HttpResponse(status=200)

    def post(self, request, *args, **kwargs):
        try:
            if "mandrill_events" in request.POST:
                events = json.loads(request.POST["mandrill_events"])
                print(events)
            else:
                return HttpResponse("Empty events", status=400)
            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)
