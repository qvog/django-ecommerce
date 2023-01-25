import json
import stripe

from django.conf import settings
from django.http import JsonResponse

from cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):
    cart = Cart(request)
    data = json.loads(request.body)

    items = []

    total_cost = 0

    for item in cart:
        product = item['product']
        total_cost += product.price * int(item['quantity'])

        items.append({
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': product.price * 100,
            },
            'quantity': item['quantity']
        })

    stripe.api_key = settings.STRIPE_API_KEY_SEC
    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/success/',
        cancel_url='http://127.0.0.1:8000/cart/'
    )

    payment_intent = session.payment_intent

    order = Order.objects.create(

        first_name = data['first_name'], 
        last_name = data['last_name'], 
        email = data['email'], 
        phone = data['phone'], 
        address = data['address'], 
        zipcode = data['zipcode'], 
        city = data['city'],
        paid = True,
        paid_amount = total_cost,
    )

    order.payment_intent = payment_intent


    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

        item = OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

    cart.clear()

    return JsonResponse({'session': session, 'order': payment_intent})