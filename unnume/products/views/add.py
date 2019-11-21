from django.shortcuts import render
from django.views.generic import FormView
from products.models import Product
from products.forms import ProductForm

class AddView(FormView):
    form_class = ProductForm
    template_name = 'products/form.html'
    success_url = '/thanks/'

