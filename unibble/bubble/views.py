from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from .models import Bubble, Unibber,User
from rest_framework.authtoken.models import Token

@api_view(
    [
        "POST"
    ]
)
def create_bubble(request):
    title = request.body["title"]
    time2meet = request.body["time2meet"]
    lat = request.body["lat"]
    lon = request.body["lon"]
    guest_num = request.body["guest_num"]
    host = Unibber.objects.get(user = request.user)
    unit = request.body["unit"]
    content = request.body["content"]
    new_bubble = Bubble(
        host = host,
        title = title,
        time2meet = time2meet,
        lat = lat,
        lon = lon,
        guest_num = guest_num,
        unit = unit,
        content = content,
    )
    new_bubble.save()
    return JsonResponse({"result" : True, "msg" : "Bubble successfully created"})

@api_view(
    [
        "GET",
    ]
)
def get_bubble(request, bubble_id):
    the_bubble = Bubble.objects.get(id = bubble_id)
    context = {
       "host" : the_bubble.host,
        "title" : the_bubble.title,
        "time2meet" : the_bubble.time2meet,
        "lat" : the_bubble.lat,
        "lon" : the_bubble.lon,
        "guest_num" : the_bubble.guest_num,
        "unit" : the_bubble.unit,
        "content" : the_bubble.content, 
    }
    return JsonResponse(context)