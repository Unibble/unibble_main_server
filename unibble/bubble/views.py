from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from unibble import bubble
from unibble.user.models import University
from .models import Bubble, Unibber

@api_view(
    [
        "GET",
    ]
)
def get_feed_bubble(request):
    units = request.GET.getlist("unit")
    bubbles = Bubble.objects.filter(is_deleted = False).all()
    if len(bubbles) == 0:
        return JsonResponse({"msg" : "There is no bubble"}, status=404)
    for code in units:
        bubbles = bubbles.filter(unit=code)
    list_response = []
    for bubble in bubbles:
        host = Unibber.objects.get(id = bubble.host)
        university = University.objects.get(id = host.university)
        host_dict = {
            "id" : host.id,
            "profileImg" : host.profile_img,
            "univName" : university.name,
            "univCampus" : university.campus,
            "major" : host.major
        }

        # 참여하기 활성화 비활성화 여부 트리거
        is_full = False
        if bubble.guest_num == bubble.guest_max:
            is_full = True

        bubble_dict = {
            "host" : host_dict,
            "unit" : bubble.unit,
            "title" : bubble.title,
            "deadline" : bubble.deadline,
            "guestNum" : bubble.guest_num,
            "guestMax" : bubble.guest_max,
            "isFull" : is_full,
        }
        list_response.append(bubble_dict)
    return JsonResponse(list_response, safe=False, status=200)

@login_required
@api_view(
    [
        "POST"
    ]
)
def create_bubble(request):
    title = request.body["title"]
    time2meet = request.body["time2meet"]
    location = request.body["location"]
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
        location = location,
        lat = lat,
        lon = lon,
        guest_num = guest_num,
        unit = unit,
        content = content,
    )
    new_bubble.save()
    return JsonResponse({"result" : True, "msg" : "Bubble successfully created"}, status=200)

@api_view(
    [
        "GET",
    ]
)
def get_bubble_detail(request, bubble_id):
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    context = {
        "host" : the_bubble.host,
        "title" : the_bubble.title,
        "time2meet" : the_bubble.time2meet,
        "lat" : the_bubble.lat,
        "lon" : the_bubble.lon,
        "guestNum" : the_bubble.guest_num,
        "unit" : the_bubble.unit,
        "content" : the_bubble.content, 
    }
    return JsonResponse(context, status=200)

@api_view(
    [
        "POST"
    ]
)
def update_bubble(request,bubble_id):
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    host = Unibber.objects.get(user = request.user)
    title = request.body["title"]
    time2meet = request.body["time2meet"]
    location = request.body["location"]
    lat = request.body["lat"]
    lon = request.body["lon"]
    guest_num = request.body["guest_num"]
    unit = request.body["unit"]
    content = request.body["content"]
    the_bubble.host = host
    the_bubble.title = title
    the_bubble.time2meet = time2meet
    the_bubble.location = location
    the_bubble.lat = lat
    the_bubble.lon = lon
    the_bubble.guest_num = guest_num
    the_bubble.unit = unit
    the_bubble.content = content
    the_bubble.save()
    return JsonResponse({"result" : True, "msg" : f"Bubble({the_bubble.id}) successfully updated"}, status=200)

@api_view(
    [
        "POST"
    ]
)
def delete_bubble(request,bubble_id):
    the_bubble = get_object_or_404(Bubble, id=bubble_id)
    the_bubble.is_deleted = True
    the_bubble.save()
    return JsonResponse({"result" : True, "msg" : f"Bubble({the_bubble.id}) successfully deleted"}, status=200)

@api_view(
    [
        "POST"
    ]
)
def participate_bubble(request, bubble_id):
    # 참여시 bubble객체의 게스트 수 +1
    the_unibber = get_object_or_404(Unibber, user = request.user)
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    the_bubble.guest = the_unibber
    the_bubble.save()
    context = {
        "result" : True,
        "msg" : f"{the_unibber.__str__()} successfully participated Bubble({the_bubble.id})"
    }
    return JsonResponse(context, status=200)

@api_view(
    [
        "POST"
    ]
)
def zzim_bubble(request, bubble_id):
    the_unibber = get_object_or_404(Unibber, user = request.user)
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    the_bubble.zzim = the_unibber
    the_bubble.save()
    context = {
        "result" : True,
        "msg" : f"{the_unibber.__str__()} successfully zzim Bubble({the_bubble.id})"
    }
    return JsonResponse(context, status=200)
