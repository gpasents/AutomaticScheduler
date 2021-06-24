from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "scheduler-home-page"),
    path('first/', views.first, name = "scheduler-first-page")
]