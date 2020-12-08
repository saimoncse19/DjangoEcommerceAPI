from django.urls import path
from .views import ProductList, home, CustomerList, OrderList

urlpatterns = [
    path('', home, name="home"),
    path('product/', ProductList.as_view(), name="product"),
    path('customer/', CustomerList.as_view(), name="customer"),
    path('order/', OrderList.as_view(), name="order")

]