from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/<int:id>/', views.menu, name="menu"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('update-status/<int:id>/', views.update_status, name="update_status"),
]
