from django.conf import settings

from product.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def __iter__(self):
        for prod in self.cart.keys():
            self.cart[str(prod)]['product'] = Product.objects.get(pk=prod)

        for item in self.cart.values():
            item['total_price'] = item['product'].price * item['quantity']

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()
    
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save
    
    def get_total_cost(self):
        for prod in self.cart.keys():
            self.cart[str(prod)]['product'] = Product.objects.get(pk=prod)

        return sum(item['product'].price * item['quantity'] for item in self.cart.values())

    def get_item(self, product_id):
        return self.cart[str(product_id)]