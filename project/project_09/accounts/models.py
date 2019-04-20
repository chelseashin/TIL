from django.shortcuts import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    
    # 절대주소로 설정하여 이 주소를 쓰면 해당 페이지에 값을 넣어 이동한다.
    def get_absolute_url(self):
        return reverse("accounts:detail", args=[self.pk])