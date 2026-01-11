from django import forms
from .models import Expenses
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'product', 'amount', 'category', 'description', 'date']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)


    class Meta:
        model= User
        fields = ('username', 'email', 'password1', 'password2')
    
        
