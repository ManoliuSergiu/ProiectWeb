from django.contrib import admin
from .models import Product, ProductDetail, ProductType, ProductTypeFeatures

admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductType)
admin.site.register(ProductTypeFeatures)

