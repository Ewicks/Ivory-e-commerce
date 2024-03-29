from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    latest_drop_page = models.BooleanField(
        default=False, null=True, blank=True)
    date_added = models.DateField(default=timezone.now)
    total_stock = models.IntegerField(null=True, blank=True, default=0)
    xs_stock = models.IntegerField(null=True, blank=True, default=0)
    s_stock = models.IntegerField(null=True, blank=True, default=0)
    m_stock = models.IntegerField(null=True, blank=True, default=0)
    l_stock = models.IntegerField(null=True, blank=True, default=0)
    xl_stock = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.name, self.product.name)
