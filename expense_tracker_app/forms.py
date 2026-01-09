from django import forms
from .models import Expenses

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'product', 'amount', 'category', 'description', 'date']