from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from .models import Unibber

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
    return JsonResponse(info)

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
    return JsonResponse(info)