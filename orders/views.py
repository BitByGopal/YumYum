from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from restaurants.models import FoodItem


@login_required
def add_to_cart(request, id):
    food = get_object_or_404(FoodItem, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Don't allow mixing items from different restaurants
    cart_items = CartItem.objects.filter(cart=cart)
    if cart_items.exists():
        old_restaurant = cart_items.first().food_item.restaurant
        if old_restaurant != food.restaurant:
            # TODO: show a proper message to user instead of silent redirect
            return redirect("cart_page")

    cart_item, created = CartItem.objects.get_or_create(cart=cart, food_item=food)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_page")


@login_required
def cart_page(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(i.food_item.price * i.quantity for i in items)

    return render(request, "cart.html", {"items": items, "total": total})


@login_required
def increase_qty(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.quantity += 1
    item.save()
    return redirect("cart_page")


@login_required
def decrease_qty(request, id):
    item = get_object_or_404(CartItem, id=id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect("cart_page")


@login_required
def remove_item(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.delete()
    return redirect("cart_page")


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(i.food_item.price * i.quantity for i in items)

    return render(request, "checkout.html", {"items": items, "total": total})


@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)

    if not items.exists():
        return redirect("cart_page")

    restaurant = items.first().food_item.restaurant
    total = sum(i.food_item.price * i.quantity for i in items)

    order = Order.objects.create(
        user=request.user,
        restaurant=restaurant,
        total_amount=total,
        delivery_address=request.user.address,
        status="pending",
    )

    for i in items:
        OrderItem.objects.create(
            order=order,
            food_item=i.food_item,
            quantity=i.quantity,
            price=i.food_item.price,
        )

    items.delete()  # clear cart after placing order

    return redirect("my_orders")


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")
    return render(request, "my_orders.html", {"orders": orders})