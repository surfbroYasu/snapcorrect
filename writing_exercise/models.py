from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from django.utils import timezone
from django.urls import reverse


from django.contrib.auth.models import User
from photos.models import Photo


class Composition(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.PROTECT
        )
    text = models.TextField(
        null=False
        )
    datetime = models.DateTimeField(
        default=timezone.now
        )
    is_solved = models.BooleanField(
        default=False
        )
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.photo_composed_count()

    # def photo_composed_count(self):
    #     photo = Photo.Objects.id
    #     compositions = Composition.objects.filter(photo=photo)
    #     total_composed = compositions.count()
    #     photo.compositioncount = total_composed
    #     photo.save()
        
    # def get_absolute_url(self):
    #     return reverse("composition_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{str(self.id)}: {self.text[:20]}"
    
class Comment(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    commenting_to = models.ForeignKey(
        Composition,
        on_delete=models.CASCADE,
        related_name="commenting_to"
        )
    text =  CKEditor5Field(
        null=True,
        blank=True,
        config_name='extends'
        )

    datetime = models.DateTimeField(
        auto_now=True
        )
    like = models.BooleanField(
        default=False
        )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f"{str(self.id)}: {self.user.username}"
    
    class Meta:
        ordering = ['-datetime']
        