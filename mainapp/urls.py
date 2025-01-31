from django.urls import path
from . import views

urlpatterns = [path("analysis", views.GetUserDoc.as_view())]
