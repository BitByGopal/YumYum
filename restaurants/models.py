from django.db import models
from accounts.models import User

class Restaurant(models.Model):
    CATEGORY_CHOICES = [
        ("biryani", "Biryani"),
        ("pizza", "Pizza"),
        ("burger", "Burger"),
        ("south", "South Indian"),
        ("north", "North Indian"),
        ("chinese", "Chinese"),
        ("dessert", "Dessert"),
    ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    open_time = models.TimeField()
    close_time = models.TimeField()

    image = models.ImageField(upload_to="restaurant_images/", null=True, blank=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="biryani")
    rating = models.FloatField(default=4.0)
    delivery_time = models.IntegerField(default=30)

    def __str__(self):
        return self.name



class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    image = models.ImageField(upload_to="food_images/", blank=True, null=True)

    def __str__(self):
        return self.item_name







