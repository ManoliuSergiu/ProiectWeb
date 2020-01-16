from django.forms import ModelForm,inlineformset_factory,BaseInlineFormSet,Form
from django.urls import reverse_lazy
from products.models import Product,ProductDetail,ProductTypeFeatures,ProductType
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','description','price','producttype']
        widgets = {
            'price': forms.NumberInput(),
            'producttype': forms.Select(attrs={'data-url':reverse_lazy('Detail Form')})
        }

class DetailForm(ModelForm):
    class Meta:
        model = ProductDetail
        fields = '__all__'

class BaseFeatureFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields['Value'] = forms.CharField()

class CartItemForm(Form):
    name= forms.CharField()
    price = forms.DecimalField()
    image = forms.FileField()
    count = forms.IntegerField()
        
DetailsFormSet = inlineformset_factory(ProductType,ProductTypeFeatures,fields=('id','name',),formset=BaseFeatureFormSet,extra=0,widgets={})