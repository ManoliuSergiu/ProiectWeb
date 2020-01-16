from django.urls import path
from . import views
from home.views import HomeView, AboutView, profile_view, CreateUser

urlpatterns = [
    path('', HomeView.as_view(), name='HomePage'),
    path('about', AboutView.as_view(), name='AboutPage'),
    path('accounts/profile/', profile_view, name='Profile'),
    path('accounts/create', CreateUser.as_view(), name='CreateUser')
]