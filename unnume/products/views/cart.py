from django.shortcuts import render
from django.views.generic import View
from products.models import Product
from django.template import RequestContext
from products.forms import CartItemForm
from django.forms import formset_factory

class CartView(View):
    template_name = 'products/cart.html'
    formset = formset_factory(form=CartItemForm,extra=0)
    def get(self,request):
        cookie = request.COOKIES.get('cart')
        items = cookie.split('/')
        aux = {}
        k=0
        for item in items:
            if item != '':
                itemId = item.split(':')[0]
                itemCount = item.split(':')[1]
                a = Product.objects.get(pk = itemId)
                aux[k] = {'name':a.name,'price':a.price,'count':itemCount,'image':a.image}
                k+=1
        return render(request,self.template_name,{'cart':aux,'count':k})
        