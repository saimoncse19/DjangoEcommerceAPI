from django.db import models
from customer.models import Customer
from product.models import Product


class Order(models.Model):
    STATUS = [
        ("In Review", "In Review"),
        ("Being Delivered", 'Being Delivered'),
        ("Cancelled", "Cancelled"),
        ('Completed', "Completed")
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.customer} - {self.status}"
