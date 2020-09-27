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
        "order_form": order_form
    }

    return render(request, template, context)
