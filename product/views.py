from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
from django.shortcuts import render
# Create your views here.

class ProductListView(ListView):
	paginate_by = 10
	model = Product


def index(request):
	return render(request, 'product/home.html')