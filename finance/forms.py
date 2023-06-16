from django import forms
from .models import Income, Expence
from bootstrap_datepicker_plus.widgets import DatePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'


class addIncomeForm(forms.ModelForm):
    
    class Meta:
        model = Income
        fields = "__all__"
        widgets = {
        'date': DateInput()
        }

class addExpenceForm(forms.ModelForm):
    
    class Meta:
        model = Expence
        fields = "__all__"
        widgets = {
        'date': DateInput()
        }