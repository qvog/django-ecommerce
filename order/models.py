from itertools import product
from django.contrib.auth.models import User
from django.db import models

from product.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    email = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount
        
        return 0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price