from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from .models import Income, Expence
from.forms import addIncomeForm, addExpenceForm
from .utils import incomeLeft
from django.db.models import Sum
from django.contrib.auth.models import User
#from djmoney.money import Money
from decimal import Decimal

# Create your views here.

def home(request):
    return render(request, "cover.html")


@login_required(login_url='login')
@permission_required("finance.can_add_income", raise_exception=True)
def income_add(request):
    if request.method == "POST":
        form = addIncomeForm(request.POST)
        if form.is_valid():
            form.save()
            #Income.get_total_amount
        return redirect('allincome')
    else:
        form = addIncomeForm()
    return render(request, 'finance/income_add.html', {'form':form})

@login_required(login_url='login')
def edit_income(request, id):
    income = get_object_or_404(Income, id=id)
    #income = Income.objects.get(id=id)
    if request.method == "POST":
        form = addIncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            #Income.get_total_amount
        return redirect('allincome')
    else:
        form = addIncomeForm()
    return render(request, 'finance/income_add.html', {'form':form, "income":income})

@login_required(login_url='login')
def delete_income(request, id):
    income = get_object_or_404(Income, pk=id)
    income.delete()
    return redirect('allincome')



@login_required(login_url='login')
@permission_required("finance.can_add_expense", raise_exception=True)
def expence_add(request):
    if request.method == "POST":
        form = addExpenceForm(request.POST)
        if form.is_valid():
            form.save()
            Expence.get_total_expense
            incomeLeft()
        return redirect("allexpense")
    else:
        form = addExpenceForm()
    return render(request, 'finance/expence_add.html', {'form':form})

@login_required(login_url='login')
def edit_expense(request, id):
    expense = get_object_or_404(Expence, id=id)
    #income = Income.objects.get(id=id)
    if request.method == "POST":
        form = addExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            #Income.get_total_amount
        return redirect('allexpense')
    else:
        form = addExpenseForm()
    return render(request, 'finance/expence_add.html', {'form':form, "expense":expense})
    
@login_required(login_url='login')
def delete_expense(request, id):
    expense = get_object_or_404(Expence, id=id)
    expense.delete()
    return redirect('allexpense')

@login_required(login_url='login')
def allincome(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    income_s = Income.objects.filter(owner__username__icontains=search_query)
    #income = Income.objects.all()
    income_sum = Income.objects.aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    expense = Expence.objects.aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    balance = incomeLeft()
    context = {"income_s": income_s, "income_sum":income_sum, "balance":balance, "expense":expense}
    return render(request, 'finance/income.html', context)

@login_required(login_url='login')
def allexpence(request):
    expense = Expence.objects.all()
    income = Income.objects.aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    expence_sum = Expence.objects.aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    balance = incomeLeft()
    context = {"expense":expense, "expence_sum":expence_sum, "income":income, "balance":balance}
    return render(request, 'finance/expences.html', context)


def loginuser(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try: 
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            messages.error(request, "username does not exist")
            return redirect('login')
        
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password is incorrect")
            return redirect('login')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')       