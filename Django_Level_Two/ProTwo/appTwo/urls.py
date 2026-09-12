from django.conf.urls import url
from django.contrib import admin
from appTwo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^admin/', admin.site.urls),
]