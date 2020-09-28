from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents

import stripe

# Create your views here.
# A view rendering chechout template.
def checkout(request):
    # Stripe required variables.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "Product not found.")
                    order.delete()
                    return redirect(reverse("cart"))
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(request, "Your form is invalid.")
    else:
        # Get cart object from session or create one if it doesn't exist.
        cart = request.session.get("cart", {})
        # Doesnt allow to load checkout screen if cart is empty.
        if not cart:
            messages.error(request, "There's nothing in your bag at the moment.")
            return redirect(reverse("products"))
        # Creating stripe payment intent.
        current_cart = cart_contents(request)
        total = current_cart["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        # Render order form and template.
        order_form = OrderForm()
    # Checking if stripe public key exists.
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is undefined.")

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret
    }

    return render(request, template, context)

def checkout_success(request, order_number):

    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Order successfuly processed! Your order number is {order_number}")

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"

    context = {
        order: order,
    }

    return render(request, template, context)