from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Unibber(models.Model):
    MAJOR = [
        ("de","Default"),
        ("im","인문계"),
        ("sh","사회계"),
        ("sk","상경계"),
        ("gy","교육계"),
        ("gh","공학계"),
        ("jy","자연계"),
        ("med","의약계"),
        ("ych","예체능"),
    ]
    STUDENT_TYPE = [
        ("newb", "신입생"),
        ("stdn", "재학생"),
        ("grad", "졸업생"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=timezone.now)
    profile_img = models.ImageField()
    major = models.CharField(max_length=3, default="de", choices=MAJOR)
    nick_name = models.TextField(max_length=10)
    phone_num = models.TextField(max_length=11)
    student_type = models.CharField(max_length=4, default="stdn", choices=STUDENT_TYPE)
    sns_link = models.TextField(max_length=20,default="연동 없음")
class University(models.Model):
    name = models.TextField(max_length=50)
    unibber = models.OneToOneField(Unibber, on_delete = models.CASCADE,null=True)
    campus = models.TextField(max_length=30, null=True)
