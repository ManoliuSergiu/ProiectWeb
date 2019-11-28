from django.forms.models import inlineformset_factory
from products.models import Product,ProductDetail,ProductTypeFeatures

Formset = inlineformset_factory(Product,ProductDetail,fields=('productTypeFeatures','Value',),can_delete=False,extra = 0)