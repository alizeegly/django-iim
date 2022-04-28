from django.urls import path
from . import views

app_name = "crud_app"
urlpatterns = [
    path("<id>/edit", views.update_view, name="edit"),
    path('show/<id>', views.detail_view, name="detail" ),
     path('<id>/delete', views.delete_view ),
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
]