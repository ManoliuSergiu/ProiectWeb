from django.shortcuts import render,reverse
from django.views.generic import UpdateView,ListView,CreateView
from products.models import Product
from products.forms import Formset

class ProductListView(ListView):
    model = Product


class ProductCreateView(UpdateView):
    model = Product
    template_name='products/form.html'
    fields =["name","description","producttype"]
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["types"] = Formset(self.request.POST,fk_name = "producttype")
        else:
            data["types"] = Formset()
        return data

    def form_valid(self,form):
        context = self.get_context_data()
        types = context["types"]
        if types.is_valid():
            types.instance = self.object.producttype
            types.save()
        return super().form_valid(form)

    def get_success_url(self):
       return reverse("parents:list")