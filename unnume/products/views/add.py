from django.shortcuts import render,reverse
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView,ListView,CreateView,View
from products.forms import ProductForm,BaseFeatureFormSet,DetailForm,DetailsFormSet
from products.models import ProductDetail,ProductTypeFeatures,ProductType,Product
from django.urls import reverse_lazy
from django import forms
from django.forms import inlineformset_factory

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name='products/form.html'

    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    
    def post(self, request):
        f = self.form_class(request.POST,request.FILES)
        if(f.is_valid()):
            prod = f.save()
            atype = ProductType.objects.get(name = f.cleaned_data['producttype'])
            fset = DetailsFormSet(request.POST,instance = atype)
            print(fset)
            print(atype)
            if(fset.is_valid()):
                print("ajunge aici")
                fset.save()
                return HttpResponseRedirect(reverse_lazy('Search'))
        return render(request, self.template_name, { 'form': self.form_class})

    

def detailFormView(request):
    aux = DetailsFormSet
    if request.method == "GET":
        atype= ProductType.objects.get(id=int(request.GET['d']))
        return render(request,'products/asd.html',{'details':aux(instance=atype)},)
    

            

        
            