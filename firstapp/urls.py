from django.urls import path
from django.conf.urls import url
from firstapp import views

urlpatterns = [
    #path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('form/', views.form_view, name='form_view'),
]