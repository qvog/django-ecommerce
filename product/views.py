from django.shortcuts import render, get_object_or_404
from .models import Product, ProductSize

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html', {'product': product})

def productsize(request):
    productsize = Product.objects.all()
    return render(request, 'product/product.html', {'productsize': productsize})



