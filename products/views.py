from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from datetime import datetime, timedelta


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.exclude(total_stock=0)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'value' in request.GET:
            query = request.GET['value']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    p = Paginator(products, 8)
    page = request.GET.get('page')
    products = p.get_page(page)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'all_products': all_products,
    }

    return render(request, 'products/products.html', context)


def latest_drop_products(request):
    products = Product.objects.all()
    latest_drop_products = products.exclude(date_added__lt=(datetime.today() - timedelta(weeks=1)))  # noqa

    context = {
        'latest_drop_products': latest_drop_products,
    }

    return render(request, 'products/latest_drops.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm(request.POST)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        print(review_form)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
        else:
            review_form = ReviewForm()

    context = {
        'product': product,
        "review_form": review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, f'Failed to '
                f'add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect('home')

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, f'Failed to update product. '
                f'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect('home')
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def delete_review(request, review_id):
    """ Delete review from the front end """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect(reverse('products'))
