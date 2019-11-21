from django import forms
from products.models import ProductType

class ProductForm(forms.Form):
    name = forms.CharField()
    image = forms.FileField()
    description = forms.CharField()  
    producttype = forms.ChoiceField(choices=[])
    def __init__(self):
        self.producttype.choices = [(x.name) for x in ProductType.objects.all()]