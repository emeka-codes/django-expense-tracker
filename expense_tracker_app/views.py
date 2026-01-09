from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from django.db.models import Sum
from .models import Expenses
from django.utils import timezone
from .forms import ExpenseForm


# Create your views here.
def display_home(request):
    form = ExpenseForm()

    if request.method == "POST":
        if 'submit_expense' in request.POST:
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/app/home')
    today = timezone.now().date()
    today_expenses = Expenses.objects.filter(date__date=today)
    today_total= today_expenses.aggregate(total=Sum("amount"))["total"] or 0

    return render(request, 'home.html', {'today_expenses': today_expenses, 'today_total': today_total, 'form': form})

def delete_expense(request):
    if request.method == "POST":
        if 'delete_expense' in request.POST:
            expense_ids = request.POST.getlist("expense_ids")
            Expenses.objects.filter(id__in=expense_ids).delete()
            return redirect("/app/home")

def edit_expense(request):
    expense_id = request.POST.get("expense_id")
    edited_expense = Expenses.objects.get(id=expense_id)
    if request.method == "POST":
        
        edited_expense.name = request.POST.get("name")
        edited_expense.product = request.POST.get("product")
        edited_expense.amount = request.POST.get("amount")
        edited_expense.category = request.POST.get("category")
        edited_expense.description = request.POST.get("description")
        edited_expense.date = request.POST.get("date")
        edited_expense.save()
        return redirect("/app/home")

def search_by_date(request):
    if request.method == "POST":
        searched_date = request.POST.get("date")
        filtered_expenses = Expenses.objects.filter(date__date=searched_date)
        total_amount = filtered_expenses.aggregate(total=Sum("amount"))["total"] or 0
        return render(request, 'home.html', {'filtered_expenses': filtered_expenses, 'total_amount': total_amount})