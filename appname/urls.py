from django.urls import path

from . import views

urlpatterns = [
    path("", views.viewname, name="viewname"),
]
