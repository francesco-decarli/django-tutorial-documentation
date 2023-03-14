# File created anew, this file is a URLconfig

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]