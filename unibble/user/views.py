from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Unibber
from user.models import University
from django.contrib.auth.decorators import login_required

@login_required
@api_view(
    [
        "GET"
    ]
)
def get_unibber(request):
    the_unibber = Unibber.objects.get(user = request.user)
    univ = University.objects.get(unibber = the_unibber)
    if univ.campus:
        campus = univ.campus
    else:
        campus = ""
    context = {
        "nickname" : the_unibber.nick_name,
        "profileImg" : the_unibber.profile_img,
        "university" : univ.name,
        "campus" : campus,
        "major" : the_unibber.major,
    }
    return JsonResponse(context, status=200)

@login_required
@api_view(
    [
        "GET"
    ]
)
def profile(request):
    the_unibber = Unibber.objects.get(user = request.user)
    univ = University.objects.get(unibber = the_unibber)
    if univ.campus:
        campus = univ.campus
    else:
        campus = ""
    bubble_participating = the_unibber.bubble_participate.all()
    bubble_host = the_unibber.bubble_host.all()
    bubble_zzim = the_unibber.bubble_zzim.all()

    bubble_participating_list = []
    bubble_host_list = []
    bubble_zzim_list = []

    for bubble in bubble_participating:
        bubble_participating_list.append(bubble.id)
    for bubble in bubble_host:
        bubble_host_list.append(bubble.id)
    for bubble in bubble_zzim:
        bubble_zzim_list.append(bubble.id)

    context = {
        "nickname" : the_unibber.nick_name,
        "profileImg" : the_unibber.profile_img,
        "university" : univ.name,
        "campus" : campus,
        "major" : the_unibber.major,
        "bubbleParticipate" : bubble_participating_list,
        "bubbleHost" : bubble_host_list,
        "bubbleZzim" : bubble_zzim_list,
    }
    return JsonResponse(context, status=200)

S3_URL = "http://unibble.s3.ap-northeast-2.amazonaws.com/"

@api_view(
    [
        "GET",
    ]
)
def get_unibber_info(request):
    unibber = Unibber.objects.get(user = request.user)
    info = {}
    info["nickname"] = unibber.nick_name
    info["profileImg"] = S3_URL+str(unibber.profile_img)
    return JsonResponse(info, status=200)

@api_view(
    [
        "GET",
    ]
)
def get_my_profile(request):
    unibber = Unibber.objects.get(user = request.user)
    info = {}
    info["email"] = unibber.user.email
    info["nickname"] = unibber.nick_name
    info["profileImg"] = S3_URL+str(unibber.profile_img)
    info["major"] = unibber.major
    info["phoneNum"] = unibber.phone_num
    info["studentType"] = unibber.student_type
    info["snsLink"] = unibber.sns_link
    return JsonResponse(info, status=200)