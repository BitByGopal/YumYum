from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Restaurant, FoodItem
from orders.models import Order, OrderItem


def home(request):
    query = request.GET.get("q")
    cat = request.GET.get("cat")

    restaurants = Restaurant.objects.all()

    if cat:
        restaurants = restaurants.filter(category=cat)

    if query:
        restaurants = restaurants.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )

    return render(request, "home.html", {"restaurants": restaurants})


def menu(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    items = FoodItem.objects.filter(restaurant=restaurant)
    return render(request, "menu.html", {"restaurant": restaurant, "items": items})


@login_required
def dashboard(request):
    restaurant = Restaurant.objects.filter(owner=request.user).first()

    if restaurant is None:
        return render(request, "dashboard.html", {"orders": []})

    orders = Order.objects.filter(restaurant=restaurant).order_by("-id")

    # Attach order items to each order so template can access them
    for order in orders:
        order.items_list = OrderItem.objects.filter(order=order)

    return render(request, "dashboard.html", {"orders": orders})


@login_required
def update_status(request, id):
    order = get_object_or_404(Order, id=id)

    status_flow = {
        "pending": "accepted",
        "accepted": "preparing",
        "preparing": "delivered",
    }

    order.status = status_flow.get(order.status, order.status)
    order.save()

    return redirect("dashboard")