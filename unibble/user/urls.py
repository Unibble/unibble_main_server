from django.urls import path
from . import views

urlpatterns = [
    path("get_unibber_info/",views.get_unibber_info,name="get_unibber_info"),
    path("get_my_profile/",views.get_my_profile,name="get_my_profile"),
]
