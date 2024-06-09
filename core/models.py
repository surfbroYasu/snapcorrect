from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class School(models.Model):
    name = models.CharField(
        max_length=75
    )
    phone = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )
    address = models.TextField(
        max_length=125,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = "profile"
    )
    birthday = models.DateField( 
        null=True,
        blank=True
        )
    image = models.ImageField(
        upload_to='user_profile/',
        null=True,
        default='sc-logo-sm-HD.png'
    )
    # teacher status extension
    is_teacher = models.BooleanField(
        default=False
    )
    organization = models.ForeignKey(
        School,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return self.user.username
    
# TODO：英語のテストや資格を登録できるテーブルを追加する
# class Accomplishment(models.Model):
#     name = models.CharField(max_length=50)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)