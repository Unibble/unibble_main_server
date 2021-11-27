from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from bubble.models import Bubble
from .models import Guest, Unibber, Zzim
from user.models import University

@api_view(
    [
        "GET"
    ]
)
def get_unibber(request):
    the_unibber = Unibber.objects.get(user = request.user)
    univ = University.objects.get(unibber = the_unibber)
    major = the_unibber.get_major_display()
    if univ.campus:
        campus = univ.campus
    else:
        campus = ""
    context = {
        "nickname" : the_unibber.nick_name,
        "profileImg" : the_unibber.profile_img.url,
        "university" : univ.name,
        "campus" : campus,
        "major" : major,
    }
    return JsonResponse(context, status=200)

@api_view(
    [
        "POST",
    ]
)
def get_unibber_info(request):
    unibber = Unibber.objects.get(user = request.user)
    info = {}
    info["nickname"] = unibber.nick_name
    info["profileImg"] = unibber.profile_img.url
    return JsonResponse(info, status=200)

@api_view(
    [
        "GET",
    ]
)
def get_my_profile(request):
    unibber = Unibber.objects.get(user = request.user)  
    major = unibber.get_major_display()
    student_type = unibber.get_student_type_display()
    info = {}
    info["email"] = unibber.user.email
    info["nickname"] = unibber.nick_name
    info["profileImg"] = unibber.profile_img.url,
    info["major"] = major,
    info["phoneNum"] = unibber.phone_num
    info["studentType"] = student_type,
    info["snsLink"] = unibber.sns_link
    return JsonResponse(info, status=200)

@api_view(
    [
        "GET",
    ]
)
def get_host_bubble(request):
    list_response = []
    the_unibber = get_object_or_404(Unibber, user = request.user)
    host_bubbles = Bubble.objects.filter(host = the_unibber)
    for bubble in host_bubbles:
        host = the_unibber
        university = host.university
        host_dict = {
            "id" : host.id,
            "profileImg" : host.profile_img.url,
            "univName" : university.name,
            "univCampus" : university.campus,
            "major" : host.get_major_display()
        }

        # 참여하기 활성화 비활성화 여부 트리거
        is_full = False
        guest_relations = Guest.objects.filter(bubble = bubble)
        if len(guest_relations) == bubble.guest_max:
            is_full = True

        bubble_dict = {
            "host" : host_dict,
            "unit" : bubble.get_unit_display(),
            "title" : bubble.title,
            "deadline" : bubble.deadline,
            "guestNum" : len(guest_relations),
            "guestMax" : bubble.guest_max,
            "isFull" : is_full,
        }
        list_response.append(bubble_dict)
        return JsonResponse(list_response, safe=False, status=200)

@api_view(
    [
        "GET",
    ]
)
def get_participate_bubble(request):
    list_response = []
    the_unibber = get_object_or_404(Unibber, user = request.user)
    guest_relations = Guest.objects.filter(unibber = the_unibber)
    participate_bubble = []
    for relation in guest_relations:
        participate_bubble.append(relation.bubble)


    for bubble in participate_bubble:
        host = bubble.host
        university = University.objects.get(id = host.university)
        host_dict = {
            "id" : host.id,
            "profileImg" : host.profile_img.url,
            "univName" : university.name,
            "univCampus" : university.campus,
            "major" : host.get_major_display()
        }

        # 참여하기 활성화 비활성화 여부 트리거
        is_full = False
        guest_relations = Guest.objects.filter(bubble = bubble)
        if len(guest_relations) == bubble.guest_max:
            is_full = True

        bubble_dict = {
            "host" : host_dict,
            "unit" : bubble.get_unit_display(),
            "title" : bubble.title,
            "deadline" : bubble.deadline,
            "guestNum" : len(guest_relations),
            "guestMax" : bubble.guest_max,
            "isFull" : is_full,
        }
        list_response.append(bubble_dict)
    return JsonResponse(list_response, safe=False, status=200)

@api_view(
    [
        "GET",
    ]
)
def get_zzim_bubble(request):
    list_response = []
    the_unibber = get_object_or_404(Unibber, user = request.user)
    zzim_relations = Zzim.objects.filter(unibber = the_unibber)
    zzim_bubble = []
    for relation in zzim_relations:
        zzim_bubble.append(relation.bubble)

    for bubble in zzim_bubble:
        host = bubble.host
        university = host.university
        host_dict = {
            "id" : host.id,
            "profileImg" : host.profile_img.url,
            "univName" : university.name,
            "univCampus" : university.campus,
            "major" : host.get_major_display()
        }
        # 참여하기 활성화 비활성화 여부 트리거
        is_full = False
        guest = Guest.objects.filter(bubble = bubble) 
        if len(guest) == bubble.guest_max:
            is_full = True

        bubble_dict = {
            "host" : host_dict,
            "unit" : bubble.get_unit_display(),
            "title" : bubble.title,
            "deadline" : bubble.deadline,
            "guestNum" : len(guest),
            "guestMax" : bubble.guest_max,
            "isFull" : is_full,
        }
        list_response.append(bubble_dict)
        return JsonResponse(list_response, safe=False, status=200)