from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, shop
from product.views import product

urlpatterns = [
    path('', include('core.urls')),
    path('product/', product, name='product'),
    path('admin/', admin.site.urls),
]
