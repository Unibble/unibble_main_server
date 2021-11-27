from django.urls import path
from . import views

urlpatterns = [
    path("get_feed_bubble/",views.get_feed_bubble,name="get_feed_bubble"),
    path("create_bubble/", views.create_bubble, name="create_bubble"),
    path("get_bubble_detail/<int:bubble_id>/", views.get_bubble_detail, name="get_bubble_detail"),
    path("update_bubble/<int:bubble_id>/",views.update_bubble,name="update_bubble"),
    path("delete_bubble/<int:bubble_id>/",views.delete_bubble,name="delete_bubble"),
    path("participate_bubble/<int:bubble_id>/", views.participate_bubble, name="participate_bubble"),
    path("zzim_bubble/<int:bubble_id>/", views.zzim_bubble, name="zzim_bubble"),
    path("create_comment/<int:bubble_id>/", views.create_comment, name="create_comment"),
    path("get_comment/<int:bubble_id>/", views.get_comment, name="get_comment"),
    path("delete_comment/<int:comment_id>/", views.delete_comment, name="delete_comment"),
]
