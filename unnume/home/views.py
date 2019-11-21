from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Contact

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'
    def get(self,request):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'home/about.html'
    