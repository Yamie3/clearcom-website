# marketing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("steward/", views.steward, name="steward"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
]
