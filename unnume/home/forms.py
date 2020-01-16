from django.forms import Form
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, CommonPasswordValidator

class CreateUserForm(Form):
    name = forms.CharField(label='Username ',max_length=20)
    password = forms.CharField(max_length=64,widget=forms.PasswordInput(),min_length=8)
    email = forms.EmailField()