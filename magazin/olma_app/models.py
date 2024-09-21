from datetime import datetime

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    WORK_TIMES = (
        ('10:00-20:00', '10:00-20:00'),
        ('09:00-19:00', '09:00-19:00'),
        ('08:00-18:00', '08:00-18:00')
    )
    address = models.CharField(max_length=256, unique=True)
    work_time = models.CharField(max_length=100, choices=WORK_TIMES)
    phone = models.CharField(max_length=13, unique=True)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    short_description = models.TextField()
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    aksiya = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Cart(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('accepted', 'accepted'),
        ('canceled', 'Canceled')
    )
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ManyToManyField(Cart)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Order #{self.id}"
