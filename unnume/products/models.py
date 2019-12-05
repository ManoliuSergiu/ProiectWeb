from django.db import models

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name = "type"
        verbose_name_plural = "types"
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.FileField(upload_to='images/',default='uploads/default.jpg')
    description = models.TextField(max_length=1000, default='Item description')
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
    def __str__(self):
        return self.name



class ProductTypeFeatures(models.Model):
    name = models.CharField(max_length=20)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "feature"
        verbose_name_plural = "features"
    def __str__(self):
        return self.name
    

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    productTypeFeatures = models.ForeignKey(ProductTypeFeatures, on_delete=models.CASCADE)
    Value = models.CharField(max_length=20)
    class Meta:
        verbose_name = "detail"
        verbose_name_plural = "details"
    def __str__(self):
        return self.Value


