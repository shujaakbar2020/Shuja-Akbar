from django.urls import path
from . import views


app_name = "Resume"

urlpatterns = [
    path('', views.index, name="index"),
    path('first/', views.first, name='first'),
]
