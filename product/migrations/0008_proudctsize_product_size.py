# Generated by Django 4.0.2 on 2023-01-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_image_ondeploy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProudctSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizeinfo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Product Sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='product.ProudctSize'),
        ),
    ]
