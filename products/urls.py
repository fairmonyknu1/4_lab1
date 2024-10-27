from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:productId>/', views.product_detail, name='product-detail'),
]
