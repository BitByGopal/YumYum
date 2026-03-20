from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.cart_page, name="cart_page"),

    path('increase/<int:id>/', views.increase_qty, name="increase_qty"),
    path('decrease/<int:id>/', views.decrease_qty, name="decrease_qty"),
    path('remove/<int:id>/', views.remove_item, name="remove_item"),

    path('checkout/', views.checkout, name="checkout"),
    path('place-order/', views.place_order, name="place_order"),
    path('my-orders/', views.my_orders, name="my_orders"),
]
