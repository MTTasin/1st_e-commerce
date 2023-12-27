from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart_detail")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_names = models.CharField(max_length=15)
    products_number = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"Order {self.id}"
    
class previous_order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_names = models.CharField(max_length=15)
    products_number = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    delivered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"