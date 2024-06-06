from django.db import models

from django.contrib.auth.models import User



class Photographer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = "photographer"
    )
    base_location = models.CharField(
        max_length=255,
        null=True
    )
    bio = models.TextField(
        max_length=1000,
        null=True
    )
    image = models.ImageField(
        upload_to='photographer_profile/',
        null=True,
        default='sc-logo-sm-HD.png'
    )
    artist_name = models.CharField(
        max_length=100,
        null=True,
    )
    
    def __str__(self):
        return f"by {self.user}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null = False,
        blank = False
    )
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(
        upload_to='images/',
        blank=False,
        null=False,
    )
    title = models.CharField(
        max_length=50,
        null=True,
        default=""
    )
    description = models.TextField(
        max_length=1000,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    photographer = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='photos'
    )
    compositionCount = models.IntegerField(
        default=0
    )
    # location
    # static_single_obj bool
    def __str__(self):
      return f"{self.title}: {self.photographer}"
        

    