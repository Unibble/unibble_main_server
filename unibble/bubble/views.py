from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from user.models import Unibber
from .models import Bubble

@api_view(
    [
        "POST"
    ]
)
def create_bubble(request):
    try:
        type = request.body["type"]
        dead_line = request.body["deadLine"]
        host = Unibber.objects.get(user = request.user)
        title = request.body["title"]
        content = request.body["content"]
        lat = request.body["lat"]
        lon = request.body["lon"]
    except KeyError:
        return JsonResponse({"result" : False,"msg" : "필수 입력 항목이 누락되었습니다."}, status_code = 402)
    new_bubble = Bubble()
    new_bubble.type = type
    new_bubble.deadline = dead_line
    new_bubble.host = host
    new_bubble.title = title
    new_bubble.content = content
    new_bubble.lat = lat
    new_bubble.lon = lon
    new_bubble.save()
    return JsonResponse({"result":True,"msg": f"Bubble object(id={new_bubble.id}) has successfully created"}, status_code = 200)