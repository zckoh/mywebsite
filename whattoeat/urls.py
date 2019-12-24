from django.urls import path
from . import views

urlpatterns = [
    path("", views.whattoeat_index, name="whattoeat_index"),
]