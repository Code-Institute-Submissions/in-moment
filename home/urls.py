from django.urls import path
from . import views

# Home page url path.
urlpatterns = [
    path("", views.index, name="home")
]
