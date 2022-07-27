from .cart import Cart

def cart(request):
    """Для глобального взаимодействия с новым классом"""
    return {'cart': Cart(request)}