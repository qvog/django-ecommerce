from django.urls import path, include

from core.views import shop, frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop')
]
