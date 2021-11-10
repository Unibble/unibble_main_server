from django.urls import path
from . import views

urlpatterns = [
    # without auth_token
    path("kakao_login/",views.kakao_login,name="kakao_login"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("check_already_signup/",views.check_already_signup, name="check_already_signup"),
    path("password_validation/",views.password_validation, name="password_validation"),
    path("check_dup_nick/",views.check_dup_nick,name="check_already_signup"),
    # need auth_token
]
