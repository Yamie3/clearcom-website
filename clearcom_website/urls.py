# clearcom_website/urls.py
from django.urls import path, include

urlpatterns = [
    path("", include("marketing.urls")),
]
