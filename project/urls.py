from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def upload(request):
    return render(request, "upload.html")


urlpatterns = [
    path("", index),  # Redirect to index.html when accessed from root URL
    path(
        "upload/", upload, name="upload"
    ),  # Render upload.html when accessed from /upload/ URL
    path("admin/", admin.site.urls),
    path("", include("mainapp.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
