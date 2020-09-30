from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, reverse

# Create your views here.
# A view to render shopping cart template.
def cart(request):
    return render(request, "cart/cart.html")

# Add items to shopping cart.
def add_to_cart(request, item_id):
    """
        Get quantity and redirect_url from post request.
        Create empty cart or get it from session if it exists.
    """
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})
    # Increase quantity of selected product if it exists in cart.
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    # Add cart to session.
    messages.success(request, "Product added to cart.")
    request.session["cart"] = cart
    return redirect(redirect_url)

# Update item quantity.
def update_cart(request, item_id):
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    messages.info(request, "Cart have been updated.")
    request.session["cart"] = cart
    return redirect(reverse("cart"))

# Remove item from cart.
def remove_from_cart(request, item_id):
    try :
        cart = request.session.get("cart", {})

        cart.pop(item_id)
        messages.info(request, "Product was removed from cart.")
        request.session["cart"] = cart
        return redirect("cart")
    except Exception as e:
        return HttpResponse(status=500)
