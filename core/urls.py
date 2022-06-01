from django.urls import path, include
from django.contrib.auth import views

from core.views import shop, frontpage, signup
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('shop/<slug:slug>/', product, name='product'),
    path('shop/', shop, name='shop'),

]
