from django.shortcuts import render
from django.views.generic import View
from products.models import Product
from django.template import RequestContext
from products.forms import CartItemForm

class CartView(View):
    template_name = 'products/cart.html'
    def get(self,request):
        cookie = request.COOKIES.get('cart')
        items = cookie.split('/')
        aux = []
        for item in items:
            if item != '':
                itemId = item.split(':')[0]
                itemCount = item.split(':')[1]
                a = Product.objects.get(pk = itemId)
                form = CartItemForm()
                form.fields['name'] = a.name
                form.fields['price'] = a.price
                form.fields['count'] = itemCount
                form.fields['image'] = a.image
                if form.is_valid():
                    aux.append(form)

        return render(request,self.template_name,{'cart':aux})