from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('user', 'base_location')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photographer, PhotographerAdmin)
admin.site.register(Photo, PhotoAdmin)