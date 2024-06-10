from django.contrib import admin
from .models import *

class JokeAdmin(admin.ModelAdmin):
    list_display = ('content', )

class JokeCommentAdmin(admin.ModelAdmin):
    list_display = ('joke', 'user')

class FavoriteJokeAdmin(admin.ModelAdmin):
    list_display = ('joke', 'user')


admin.site.register(Joke, JokeAdmin)
admin.site.register(JokeComment, JokeCommentAdmin)
admin.site.register(FavoriteJoke, FavoriteJokeAdmin)