from django.contrib import admin

from .models import Category, Product, ProductSize

admin.site.register(Category)
admin.site.register(Product)

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['sizeinfo',]





