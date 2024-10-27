from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm
from .models import Expense


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


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 重定向到首页或其他页面
            else:
                form.add_error(None, "账号和密码不正确，请重新输入")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 可能需要登录用户或重定向到登录页面
            return redirect('login')  # 确保你有一个名为 'login' 的 URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'expenses/register.html', {'form': form})
