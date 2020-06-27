from django.urls import path
from product.views import ProductListView

urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-list'),
]