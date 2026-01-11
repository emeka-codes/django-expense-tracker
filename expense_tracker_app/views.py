from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from django.db.models import Sum
from .models import Expenses
from django.utils import timezone
from .forms import ExpenseForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/app/login')
def display_home(request):
    form = ExpenseForm()

    if request.method == "POST":
        if 'submit_expense' in request.POST:
            form = ExpenseForm(request.POST)
            if form.is_valid():
                expense= form.save(commit=False)
                expense.user= request.user
                expense.save()
                return redirect('/app/home')
    today = timezone.now().date()
    today_expenses = Expenses.objects.filter(user= request.user, date__date=today)
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
        filtered_expenses = Expenses.objects.filter(user= request.user, date__date=searched_date)
        total_amount = filtered_expenses.aggregate(total=Sum("amount"))["total"] or 0
        return render(request, 'home.html', {'filtered_expenses': filtered_expenses, 'total_amount': total_amount})
    
def user_login(request):
    if request.method == "POST":
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/app/home')
            else:
                return HttpResponse("Invalid credentials")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/app/home')

def user_signup(request):
    form = SignUpForm(request.POST)
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            
            return redirect('/app/home')
    return render(request, 'signup.html', {'form': form})
   
