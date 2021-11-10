from django.urls import path
from . import views

urlpatterns = [
    path("kakao_login/",views.kakao_login,name="kakao_login"),
    #path("login/",views.)
]
