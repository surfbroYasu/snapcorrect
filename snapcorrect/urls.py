"""
画像のアップロードや写真を寄贈してくれる人のアプリ
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import urls as core_urls
from photos import urls as photos_urls
from writing_exercise import urls as writing_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("__debug__/", include("debug_toolbar.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
    
    path("", include(core_urls, namespace="core")),
    path("photo/", include(photos_urls, namespace="photos")),
    path("writing/", include(writing_urls, namespace="writing")),
    
    path('accounts/', include('allauth.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
if not settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
