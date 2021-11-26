from django.urls import path
from . import views

urlpatterns = [
    path("get_feed_bubble/",views.get_feed_bubble,name="get_feed_bubble"),
    path("create_bubble/", views.create_bubble, name="create_bubble"),
    path("get_bubble/<int:bubble_id>/", views.get_bubble, name="get_bubble"),
    path("participate_bubble/<int:bubble_id>/", views.participate_bubble, name="participate_bubble"),
    path("zzim_bubble/<int:bubble_id>/", views.zzim_bubble, name="zzim_bubble"),
]
