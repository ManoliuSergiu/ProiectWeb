from django.shortcuts import render
from django.views.generic import DetailView
from products.models import Product

class ItemView(DetailView):
    queryset = Product.objects.all()

