from django.urls import path
from . import views

app_name = 'letschat_app'

urlpatterns = [
    path('',  views.index, name="index"),
    path('<str:name>/', views.room_name, name='room'),
]