from django.urls import path
from twitter import views

urlpatterns = [
    path('', views.index, name='index')
]
