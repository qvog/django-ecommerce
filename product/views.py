from django.shortcuts import render, get_object_or_404
from .models import Product

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html', {'product': product})

def get_size(request, product_size):
    size = Product.objects.get(pk=product_size)
    
    if request.POST:
        sizeid = request.POST.get('Size')
        print('asdasda', sizeid)

    return render(request, 'product/product.html')
