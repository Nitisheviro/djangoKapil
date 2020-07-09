from django.urls import path
from product.views import ProductListView, index

urlpatterns = [
    path('', index, name='product-home'),
    path('home', index, name='product-home'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
]