from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class Product(models.Model):

    name = models.CharField(verbose_name="Product Name", max_length=250)
    description = models.TextField(verbose_name="Product Description")
    price = models.IntegerField(verbose_name="Price")
    is_discounted = models.BooleanField(verbose_name="Is Discounted?", default=False)
    discounted_price = models.IntegerField(verbose_name="Discounted Price", null=True, blank=True)
    available_colors = models.ManyToManyField(verbose_name="Available Colors", to=Color)
    available_sizes = models.ManyToManyField(verbose_name="Available Sizes", to=Size)
    rating = models.FloatField(verbose_name="Rating")
    thumbnail = models.URLField(verbose_name="Thumbnail")

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.URLField(verbose_name="Image")
