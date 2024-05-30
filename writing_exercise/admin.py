from django.contrib import admin
from .models import *

class CompositionAdmin(admin.ModelAdmin):
    list_display = ('author', 'datetime', "is_solved", "id")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'commenting_to', 'parent')
    



admin.site.register(Composition, CompositionAdmin)
admin.site.register(Comment, CommentAdmin)

