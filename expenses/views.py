from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm
from .models import Expense
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')  # 重定向未登录用户到登录页面
def list_expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/list_expense.html', {'expenses': expenses})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/form_expense.html', {'form': form})


def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/form_expense.html', {'form': form})


def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('list_expenses')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # 将用户重定向到首页或其他页面
    else:
        form = RegisterForm()
    return render(request, "expenses/register.html", {"form": form})
