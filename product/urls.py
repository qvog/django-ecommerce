from django.urls import path

from .views import get_size
urlpatterns = [
    path('get_size/<str:product_size>/', get_size, name='get_size'),
]