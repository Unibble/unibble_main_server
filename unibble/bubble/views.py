from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from user.models import Unibber, Zzim, Guest 
from .models import Bubble, Comment
from datetime import datetime, timedelta

@api_view(
    [
        "GET",
    ]
)
def get_feed_bubble(request):
    units = request.GET.getlist("unit")
    total_bubbles = []
    for unit in units:
        bubbles = Bubble.objects.filter(Q(is_deleted = False)&Q(unit = int(unit))).all()
        total_bubbles += bubbles
    print(f"total_bubbles :{total_bubbles}")
    list_response = []
    for bubble in total_bubbles:
        host = bubble.host
        university = host.university
        guest = Guest.objects.filter(bubble = bubble).all()
        host_dict = {
            "nick_name" : host.nick_name,
            "profileImg" : host.profile_img.url,
            "univName" : university.name,
            "univCampus" : university.campus,
            "major" : host.get_major_display()
        }

        # 참여하기 활성화 비활성화 여부 트리거
        is_full = False
        if len(guest) == bubble.guest_max:
            is_full = True

        bubble_dict = {
            "host" : host_dict,
            "unit" : bubble.unit,
            "title" : bubble.title,
            "deadline" : bubble.deadline,
            "guestNum" : len(guest),
            "guestMax" : bubble.guest_max,
            "isFull" : is_full,
        }
        list_response.append(bubble_dict)
    return JsonResponse(list_response, safe=False, status=200)

@api_view(
    [
        "POST"
    ]
)
def create_bubble(request):
    title = request.data["title"]
    time2meet = request.data["time2meet"]
    deadline = datetime.strptime(time2meet, "%Y-%m-%d %H:%M:%S") + timedelta(days=1)
    location = request.data["location"]
    address = request.data["address"]
    lat = request.data["lat"]
    lon = request.data["lon"]
    guest_max = request.data["guest_max"]
    host = Unibber.objects.get(user = request.user)
    unit = request.data["unit[]"]
    content = request.data["content"]
    new_bubble = Bubble(
        host = host,
        title = title,
        time2meet = time2meet,
        deadline = deadline,
        address = address,
        location = location,
        lat = lat,
        lon = lon,
        guest_max = guest_max,
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

    # host 정보
    host = the_bubble.host
    university = host.university
    host_dict = {
            "nick_name" : host.nick_name,
            "profileImg" : str(host.profile_img.url),
            "univName" : university.name,
            "univCampus" : university.campus,
            "major" : host.get_major_display()
        }

    # guest 정보
    guest_list = []
    guest_relation = Guest.objects.filter(bubble = the_bubble)
    for relation in guest_relation:
        guest_dict = {
            "nickname" : relation.unibber.nickname,
            "profileImg" : relation.unibber.profile_img,
        }
        guest_list.append(guest_dict)

    context = {
        "host" : host_dict,
        "title" : the_bubble.title,
        "time2meet" : the_bubble.time2meet,
        "location" : the_bubble.location,
        "guest" : guest_list,
        "guestNum" : len(guest_relation),
        "guestMax" : the_bubble.guest_max,
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
    title = request.data["title"]
    time2meet = request.data["time2meet"]
    location = request.data["location"]
    address = request.data["address"]
    lat = request.data["lat"]
    lon = request.data["lon"]
    guest_max = request.data["guest_max"]
    unit = request.data["unit[]"]
    content = request.data["content"]
    the_bubble.host = host
    the_bubble.title = title
    the_bubble.time2meet = time2meet
    the_bubble.location = location
    the_bubble.address = address,
    the_bubble.lat = lat
    the_bubble.lon = lon
    the_bubble.guest_max = guest_max
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
    the_unibber = get_object_or_404(Unibber, user = request.user)
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    new_guest = Guest(unibber = the_unibber, bubble = the_bubble)
    new_guest.save()
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
    new_zzim = Zzim(unibber = the_unibber, bubble = the_bubble)
    new_zzim.save()
    context = {
        "result" : True,
        "msg" : f"Bubbler({the_unibber.id}) successfully zzim Bubble({the_bubble.id})"
    }
    return JsonResponse(context, status=200)

@api_view(
    [
        "POST"
    ]
)
def create_comment(request, bubble_id):
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    writer = get_object_or_404(Unibber, user = request.user)
    content = request.data["content"]
    if len(content) == 0:
        return JsonResponse({"msg" : f"Empty content"}, status=404)    
    new_comment = Comment(writer = writer, bubble = the_bubble, content=content)
    new_comment.save()
    return JsonResponse({"msg" : f"Comment successfully written"}, status=200)

@api_view(
    [
        "GET"
    ]
)
def get_comment(request, bubble_id):
    the_bubble = get_object_or_404(Bubble, id = bubble_id)
    comments = Comment.objects.filter(bubble = the_bubble)
    list_response = []
    for comment in comments:
        is_host = comment.writer == the_bubble.host
        is_participate = Guest.objects.filter(bubble = the_bubble, unibber = comment.writer).exists()
        comment_dict = {
            "profileImg" : comment.writer.profile_img.url,
            "nickName" : comment.writer.__str__(),
            "university" : comment.writer.university.name,
            "campus" : comment.writer.university.campus,
            "major" : comment.writer.get_major_display(),
            "is_participate" : is_participate,
            "is_host" : is_host,
            "created" : comment.created,
            "content" : comment.content
        }
        list_response.append(comment_dict)
    return JsonResponse(list_response, safe=False, status=200)

@api_view(
    [
        "DELETE"
    ]
)
def delete_comment(request, comment_id):
    current_unibber = get_object_or_404(Unibber, user = request.user)
    the_comment = get_object_or_404(Comment, id = comment_id)
    if the_comment.writer == current_unibber:
        the_comment.delete()
        return JsonResponse({"msg" : f"Comment successfully deleted"}, status=200)
    else:
        return JsonResponse({"msg" : f"Only writer can delete his/her comment"}, status=400)
