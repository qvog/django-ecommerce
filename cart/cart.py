from django.conf import settings

from product.models import Product

class Cart(object):
    
    def __init__(self, request):
        """Инициализация сессии и проверка на существование корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart #Для дальнейшего использования в других методах этого класса

    def __iter__(self):
        """Цикл для доступа к Product из бд и увелечение стоимости в соответствии с кол-во продукта"""
        for prod in self.cart.keys():
            self.cart[str(prod)]['product'] = Product.objects.get(pk=prod)

        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity'])

            yield item

    def __len__(self):
        """Для измерения кол-во предметов в корзине"""
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        """Обновление сеанса для пользователя, при редактировании корзины"""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        """Добавление в корзину """

        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id}
        
        if update_quantity: 
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()
    
    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]

        self.save

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        """Получение всей стоимости корзины"""
        for prod in self.cart.keys():
            self.cart[str(prod)]['product'] = Product.objects.get(pk=prod)

        return sum(item['product'].price * item['quantity'] for item in self.cart.values())

    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None