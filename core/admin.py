from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(School, SchoolAdmin)