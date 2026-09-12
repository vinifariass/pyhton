from importlib.resources import path

from django.urls import path
from django.contrib import admin
from appTwo import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
    path("admin/", admin.site.urls),
]