from django.urls import path

from . import views

app_name = 'gitReq'
urlpatterns = [
    path('', views.index, name='index')
]