import json
import stripe

from django.shortcuts import render, redirect
from django.conf import settings

from cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):
    cart = Cart(request)

#see u later..