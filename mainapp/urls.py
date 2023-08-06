from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetUserDoc.as_view())
]