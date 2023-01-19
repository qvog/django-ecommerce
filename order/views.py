import json
import stripe

from django.shortcuts import render, redirect
from django.conf import settings

from cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):
    cart = Cart(request)
    data = json.loads(request.body)

    items = []

    total_cost = 0

    for item in cart:
        product = item['product']
        total_cost += product.price * int(item('quantity'))

        items.append({
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': product.price,
            },
            'quantity': item['quantity']
        })

