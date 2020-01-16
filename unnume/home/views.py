from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from .models import Contact
from .forms import CreateUserForm
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'
    def get(self,request):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'home/about.html'
    

    
def profile_view(request):
    template_name = 'home/profile.html'
    return render(request,template_name)

class CreateUser(CreateView):
    form_class = CreateUserForm
    template_name='registration/registration.html'
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            user = User.objects.create_user(username=form.cleaned_data['name'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])
        return HttpResponseRedirect(redirect_to='login')
            



