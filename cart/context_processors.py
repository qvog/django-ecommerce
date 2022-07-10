from .cart import Cart

"""Для глобального взаимодействия с новым классом"""
def cart(request):
    return {'cart': Cart(request)}