from django.urls import path
from .views import home, new_view

urlpatterns = [
    path("", home, name = "home"),
    path("drugi/", new_view, name = 'new'),
]