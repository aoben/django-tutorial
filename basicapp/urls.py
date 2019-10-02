
from django.urls import path
from django.conf.urls import url, include
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path("index/", views.index, name='index'),
    path("other/", views.other, name='other'),
    path("relative/", views.relative, name='relative'),
    path("register/", views.register, name='register'),
    path("userlogout/", views.userlogout, name='userlogout'),
    path("userlogin/", views.userlogin, name='userlogin'),
]