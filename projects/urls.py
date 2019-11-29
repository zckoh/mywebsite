from django.urls import path
from . import views

# app_name = 'projects'
urlpatterns = [
    path("", views.projects_index, name="projects_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]