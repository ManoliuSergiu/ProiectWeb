from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.views.generic import UpdateView,ListView,CreateView
from products.models import Product
from django.urls import reverse_lazy
from django import forms

class ProductListView(ListView):
    model = Product



class ProductCreateView(CreateView):
    model = Product
    template_name='products/form.html'
    fields =["name","image","description","producttype"]
    widgets = {
        'producttype': forms.Select(attrs={"class":"btn"})
    }
    
def homeDynamicContent(request):
    return HttpResponse('success')