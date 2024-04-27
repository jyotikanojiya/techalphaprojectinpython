from django.shortcuts import render, redirect
from .models import Expense, Category
from .forms import ExpenseForm , CategoryForm
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'clist.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'addc.html', {'form': form})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add.html', {'form': form})
