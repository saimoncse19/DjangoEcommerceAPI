from django.views.generic import ListView
from product.models import Product
from customer.models import Customer
from order.models import Order
from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


class ProductList(ListView):
    model = Product
    template_name = "pages/product.html"
    context_object_name = "products"


class CustomerList(ListView):
    model = Customer
    template_name = 'pages/customer.html'
    context_object_name = "customers"


class OrderList(ListView):
    model = Order
    template_name = 'pages/order.html'
    context_object_name = "orders"
