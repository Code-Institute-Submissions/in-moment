from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
# A view rendering chechout template.
def checkout(request):
    # Get cart object from session or create one if it doesn't exist.
    cart = request.session.get("cart", {})
    # Doesnt allow to load checkout screen if cart is empty.
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse("products"))
    # Render order form and template.
    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51HWFFLD66EYFz3UhxITVEovAb75FM6HWfTPQc9F3Jgeq6okW240P3McUe9xwa8xwCT0pAR1AAiiE9E2I6N9PlDyI00l3Bt9KDY",
        "client_secret": "test_client_secret",
    }

    return render(request, template, context)
