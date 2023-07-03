from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from decimal import Decimal

# Create your models here.
class Income(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amount= MoneyField(max_digits=14, decimal_places=2, default_currency='NGN', default=0.00)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} deposited by {self.owner}"
    class Meta:
        ordering =['-date']
    
    # @property
    # def get_total_income():
    #     #total_amount = self.objects.aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    #     total_amount = self.objects.aggregate(total=Sum('amount')).get('total')
    #     return total_amount

class Expence(models.Model):
    title = models.CharField(max_length=50)
    #amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='NGN', default=0.00)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} spent on {self.title}"

    class Meta:
        ordering = ["-date"]

    # @property
    # def get_total_expense():
    #     #total_exp = self.objects.aggregate(total=Sum('amount')).get('total', Decimal('0.00'))
    #     total_exp = self.objects.aggregate(total=Sum('amount')).get('total')
    #     return total_exp
