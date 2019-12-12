from django.db import models

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=20)
    objects = models.Manager()
    class Meta:
        verbose_name = "type"
        verbose_name_plural = "types"
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FileField(upload_to='images/',default='uploads/default.jpg')
    description = models.TextField(max_length=1000, default='Item description')
    objects = models.Manager()
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
    def __str__(self):
        return self.name

class ProductTypeFeatures(models.Model):
    name = models.CharField(max_length=20)
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    objects = models.Manager()
    class Meta:
        verbose_name = "feature"
        verbose_name_plural = "features"
    def __str__(self):
        return self.name
    

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    feature = models.ForeignKey(ProductTypeFeatures, on_delete=models.CASCADE, related_name='details')
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=True)
    Value = models.CharField(max_length=20)
    objects = models.Manager()
    class Meta:
        verbose_name = "detail"
        verbose_name_plural = "details"
    def __str__(self):
        return self.Value



