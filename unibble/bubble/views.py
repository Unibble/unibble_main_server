from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .models import Bubble, Unibber

@login_required
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

@api_view(
    [
        "POST"
    ]
)
def participate_bubble(request, bubble_id):
    the_unibber = Unibber.objects.get(user = request.user)
    the_bubble = Bubble.objects.get(id = bubble_id)
    the_bubble.guest = the_unibber
    the_bubble.save()
    context = {
        "result" : True,
        "msg" : f"{the_unibber.__str__()} successfully participated Bubble({the_bubble.id})"
    }
    return JsonResponse(context)

@api_view(
    [
        "POST"
    ]
)
def zzim_bubble(request, bubble_id):
    the_unibber = Unibber.objects.get(user = request.user)
    the_bubble = Bubble.objects.get(id = bubble_id)
    the_bubble.zzim = the_unibber
    the_bubble.save()
    context = {
        "result" : True,
        "msg" : f"{the_unibber.__str__()} successfully zzim Bubble({the_bubble.id})"
    }
    return JsonResponse(context)
