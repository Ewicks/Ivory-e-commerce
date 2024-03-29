from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('latest_drops/', views.latest_drop_products, name='latest_drop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # noqa
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),  # noqa
]
