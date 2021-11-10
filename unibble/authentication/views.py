from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from user.models import Unibber,User
from rest_framework.authtoken.models import Token
import logging
import json

logger = logging.getLogger(__name__)

def kakao_login(request):
    try:
        # FE로부터 kakako token 받기
        kakao_token = request.headers.get("Authorization")
        
        if kakao_token == None:
            return JsonResponse({"message" : '토큰이 유효하지 않습니다'},status=401)
        
        # kakao token을 다시 kakao로 보내서 유저 정보를 받아옵니다.
        kakao_account = requests.get(
            'https://kapi.kakao.com/v2/user/me',
            headers = {'Authorization': f'Bearer {kakao_token}'}).json()
        print(f"kakao_account : {kakao_account}")
        # 가져온 kakao 계정의 id가 db에 존재 하는지 확인
        if not User.objects.filter(email = kakao_account['kakao_account']['email']).exists():
            # 유저 정보가 없으면 회원가입
            user = User.objects.create(
                email = kakao_account['kakao_account']['email']
            )
            user.save()
            unibber = Unibber.objects.create(user=user)
            unibber.save()
            token = Token.objects.create(user=user)
            json_response = json.dumps({'auth_token': token})
            return JsonResponse(json_response, status=201)
        user = User.objects.get(email = kakao_account['kakao_account']['email'])
        token = Token.objects.get(user=user)
        json_response = json.dumps({'auth_token': token})
        return JsonResponse(json_response, status=200)
    except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
    except ConnectionError:
        return JsonResponse({'message': 'CONNECTION_ERROR'}, status=400)

api_view(
    [
        "POST"
    ]
)
def signup(request):
    email = request.data["email"]
    pw = request.data["pw1"]
    pw = request.data["pw2"]
