from django.forms import ModelForm,inlineformset_factory,BaseInlineFormSet
from django.urls import reverse_lazy
from products.models import Product,ProductDetail,ProductTypeFeatures,ProductType
from django import forms

DetailsFormSet = inlineformset_factory(ProductType,ProductTypeFeatures,fields=('name',),extra=0,widgets={})

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','description','price','producttype']
        widgets = {
            'producttype': forms.Select(attrs={'data-url':reverse_lazy('Detail Form')})
        }


class BaseFeatureFormSet(BaseInlineFormSet):

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields['Value'] = forms.CharField()