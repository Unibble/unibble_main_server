from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
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
    
    def __str__(self) -> str:
        str_name = ''
        if self.nick_name:
            str_name = self.nick_name
        else:
            str_name = self.user.email
        return str_name
class University(models.Model):
    name = models.TextField(max_length=50)
    unibber = models.OneToOneField(Unibber, on_delete = models.CASCADE,null=True)
    campus = models.TextField(max_length=30, null=True)
