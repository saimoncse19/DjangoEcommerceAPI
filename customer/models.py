from django.db import models


class Address(models.Model):
    NAMES = [
        ('Home', 'Home'),
        ("Permanent", 'Permanent')

    ]
    name = models.CharField(choices=NAMES, default="Permanent", max_length=20)
    street = models.CharField(max_length=250)
    town = models.CharField(max_length=250)
    zip_or_postal = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=14, null=True)
    email = models.EmailField()
    permanent_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    profile_picture = models.URLField(null=True)

    def __str__(self):
        return self.name
