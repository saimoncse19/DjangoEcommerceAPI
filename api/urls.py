from django.urls import path
from .views import ProductList, ProductDetail, CustomerList, CustomerDetail, OrderDetail, OrderList

urlpatterns = [
    path('product/', ProductList.as_view(), name="product_list"),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('customer/', CustomerList.as_view(), name="customer_list"),
    path('customer/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
    path('order/', OrderList.as_view(), name="order_list"),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail')

]