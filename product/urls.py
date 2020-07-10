from django.urls import path
from product.views import ProductListView, index, aboutus

urlpatterns = [
    # path('', index, name='product-home'),
    # path('home', index, name='product-home'),
    path('', ProductListView.as_view(), name='product-list'),
    path('aboutus', aboutus, name='aboutus'),
]