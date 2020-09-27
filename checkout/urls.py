from django.urls import path
from . import views

# All urls assosiated with checkout.
urlpatterns = [
    path("", views.checkout, name="checkout")
]
