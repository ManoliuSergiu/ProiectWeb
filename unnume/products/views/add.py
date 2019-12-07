from django.shortcuts import render,reverse
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import UpdateView,ListView,CreateView,View
from products.forms import ProductForm,BaseFeatureFormSet
from products.models import ProductDetail,ProductTypeFeatures,ProductType,Product
from django.urls import reverse_lazy
from django import forms
from django.forms import inlineformset_factory

class ProductCreateView(CreateView):
    template_name='products/form.html'


    def get(self, request):
        form = ProductForm()
        return render(request,self.template_name,{'form':form})

    

def detailFormView(request):
    aux = inlineformset_factory(ProductType,ProductTypeFeatures,fields=('name',),extra=0,widgets={},formset=BaseFeatureFormSet,can_delete=False)
    atype= ProductType.objects.get(id=int(request.GET['d']))
    return render(request,'products/asd.html',{'details':aux(instance=atype)},)

def save(request):
    if(request.method == 'POST'):
        productform = ProductForm(request.POST['prodform'])
        
        a = productform['name']
        return a
        
            