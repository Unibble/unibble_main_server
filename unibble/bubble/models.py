from django.db import models
from django.utils import timezone

class Bubble(models.Model):
    BUBBLE_TYPE = [
        ("live", "대기중"),
        ("confirmed","확정됨"),
        ("expired","만료됨"),
    ]
    UNIT = [
        (0,"밥"),
        (1,"술"),
        (2,"미팅"),
        (3,"스터디"),
        (4,"영화"),
        (5,"운동"),
        (6,"산책"),
        (7,"게임"),
        (8,"기타"),
    ]
    type = models.CharField(max_length=10, default="live", choices=BUBBLE_TYPE)
    created = models.DateTimeField(auto_now=timezone.now)
    time2meet = models.DateTimeField()
    deadline = models.DateTimeField()
    host = models.ForeignKey("user.Unibber", on_delete=models.CASCADE)
    guest_max = models.PositiveSmallIntegerField(default=0)
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=500,null=True, blank=True)
    unit = models.PositiveSmallIntegerField(blank=True, choices=UNIT)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100,blank=True)
    address = models.TextField(max_length=200,null=True, blank=True)
    is_deleted = models.BooleanField(default=False)


class Comment(models.Model):
    created = models.DateTimeField(auto_now=timezone.now)
    writer = models.ForeignKey("user.Unibber", on_delete=models.CASCADE)
    bubble = models.ForeignKey(Bubble, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)