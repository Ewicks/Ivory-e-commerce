from django.shortcuts import render, redirect
from django.contrib import messages


def all_products(request):

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    return render(request, 'products/product_detail.html', context)
