from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    return render(request, 'products/product_detail.html', {})
