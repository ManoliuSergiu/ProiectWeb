from django.db import models

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='uploads/',default='uploads/default.jpg')
    description = models.TextField(max_length=1000, default='Item description')


class Product(models.Model):
    name = models.CharField(max_length=100)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class ProductTypeFeatures(models.Model):
    name = models.CharField(max_length=20)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    productTypeFeatures = models.ForeignKey(ProductTypeFeatures, on_delete=models.CASCADE)
    Value = models.CharField(max_length=20)


