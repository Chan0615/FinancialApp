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
