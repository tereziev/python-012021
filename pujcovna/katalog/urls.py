from django.urls import path
from . import views
from django.views.generic import ListView


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("seznam/", views.SeznamView.as_view(), name="seznam")
]