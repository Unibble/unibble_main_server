from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from .models import Unibber

@api_view(
    [
        "GET",
    ]
)
def get_unibber_info(request):
    unibber = Unibber.objects.get(user = request.user)
    info = {}
    info["nickname"] = unibber.nickname
    info["profileImg"] = unibber.profile_img
    return JsonResponse(info)

@api_view(
    [
        "GET",
    ]
)
def get_my_profile(request):
    unibber = Unibber.objects.get(user = request.user)
    info = {}
    info["nickname"] = unibber.nickname
    info["profileImg"] = unibber.profile_img
    return JsonResponse(info)