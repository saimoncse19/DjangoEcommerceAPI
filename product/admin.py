from django.contrib import admin
from .models import ProductImage, Product, Color, Size


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]


admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)