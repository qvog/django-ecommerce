from django import forms
from django.db import models
from django.core.files import File
from django import forms

from PIL import Image
from io import BytesIO

class Category(models.Model):
    """Категория товаров"""
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', )
    
    def __str__(self):
        return self.name

class ProductSize(models.Model):
    sizeinfo = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Product Sizes'

    def __str__(self):
        return self.sizeinfo

class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    discription = models.TextField(blank=True, null=True)
    size = models.ManyToManyField(ProductSize)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_ondeploy = models.URLField(max_length=200, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    def get_display_price(self):
        return self.price

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        """Автоматическое создание маленького изображения, после загрузки обычного"""
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name




    


