from django.urls import path
from . import views

urlpatterns = [
    path("get_unibber/",views.get_unibber,name="get_unibber"),
    path("get_unibber_info/",views.get_unibber_info,name="get_unibber_info"),
    path("get_my_profile/",views.get_my_profile,name="get_my_profile"),
    path("get_host_bubble/",views.get_host_bubble,name="get_host_bubble"),
    path("get_participate_bubble/",views.get_participate_bubble,name="get_participate_bubble"),
    path("get_zzim_bubble/",views.get_zzim_bubble,name="get_zzim_bubble"),
]
