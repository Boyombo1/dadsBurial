from .models import Income, Expence
from django.db.models import Sum
from djmoney.money import Money
from decimal import Decimal

# def incomeLeft():
#     total_income = Income.objects.aggregate(total=Sum('amount')).get('total', Money('0.00'))
#     total_expenses = Expence.objects.aggregate(total=Sum('amount')).get('total', Money('0.00'))
    
#     if total_income is None:
#         total_income = Decimal('0.00')
    
#     if total_expenses is None:
#         total_expenses = Decimal('0.00')

#     income_left = total_income - total_expenses
#     return income_left
def incomeLeft():
    total_income = Income.objects.aggregate(total=Sum('amount')).get('total')
    total_expenses = Expence.objects.aggregate(total=Sum('amount')).get('total')

    income_left = total_income - total_expenses
    return income_left