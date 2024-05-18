from django.urls import path

from . import views

app_name = "Clinica"

urlpatterns = [
    path("", views.index, name="index"),
   
]
