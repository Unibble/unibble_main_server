from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator,CommonPasswordValidator,NumericPasswordValidator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests
from user.models import Unibber,User
from rest_framework.authtoken.models import Token
import logging

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
            return JsonResponse({'authToken': token.key, "status": 200},status=200)
        user = User.objects.get(email = kakao_account['kakao_account']['email'])
        token = Token.objects.get(user=user)
        return JsonResponse({'authToken': token.key, "status" : 200},status=200)
    except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
    except ConnectionError:
        return JsonResponse({'message': 'CONNECTION_ERROR'}, status=400)

@login_required
def after_kakao(request):
    the_unibber = Unibber.objects.get(user = request.user)
    univ_img = request.FILES["univImg"]
    nickname = request.body["nickname"]
    phone_num = request.body["phone_num"]
    student_type = request.body["student_type"]
    the_unibber.univ




def login(request):
    email = request.body["email"]
    password = request.body["password"]
    user = User.objects.get(email=email, password=password)
    token = Token.objects.get(user=user)
    if user:
        login(request,user)
        return JsonResponse({"result" : True,"authToken" : token.key,"msg" : f"{user.__str__()} logged in"})
    else:
        return JsonResponse({"result" : False,"msg" : "login failed"})

def signup(request):
    email = request.body["email"]
    if User.objects.get(email = email).exits():
        return JsonResponse({"msg" : "already has account"})
    pw1 = request.body["pw1"]
    pw2 = request.body["pw2"]
    nick_name = request.body["nick_name"]
    if Unibber.objects.get(nick_name = nick_name).exists():
        return JsonResponse({"msg" : "duplicate nickname"})
    phone_num = request.body["phone_num"]
    student_type = request.body["student_type"]
    if pw1 == pw2:
        user = User(email = email, password=pw1)
        user.save()
        token = Token.objects.create(user=user)
        unibber = Unibber(
            user=user,
            nick_name = nick_name,
            phone_num = phone_num,
            student_type = student_type,
                # ("newb", "신입생"),
                # ("stdn", "재학생"),
                # ("grad", "졸업생"),
            )
        unibber.save()
        # login after signup
        login(request,user)
        return JsonResponse({"authToken" : token.key,"msg" : "unibber successfuly created"})
    else:
        return JsonResponse({"msg" : "password not same"})

# validation APIs

def check_already_signup(request):
    email = request.body["email"]
    if User.objects.get(email = email).exits():
        return JsonResponse({"hasAccount" : True })
    else:
        return JsonResponse({"hasAccount" : False })

def password_validation(request):
    password = request.body["password"]
    try:
        # using django default password validator
        UserAttributeSimilarityValidator.validate(password=password)
        MinimumLengthValidator.validate(password=password)
        CommonPasswordValidator.validate(password=password)
        NumericPasswordValidator.validate(password=password)
    except:
        return JsonResponse({"pwCheck" : False})
    return JsonResponse({"pwCheck" : True})


def check_dup_nick(request):
    nick_name = request.body["nick_name"]
    if Unibber.objects.get(nick_name = nick_name).exits():
        return JsonResponse({"dupNick" : True })
    else:
        return JsonResponse({"dupNick" : False })
