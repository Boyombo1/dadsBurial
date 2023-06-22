from django.urls import path, include
from . import views

urlpatterns = [
    path('addincome/', views.income_add, name='addincome'),
    path('addexpense/', views.expence_add, name='addexpense'),
    path('allexpense/', views.allexpence, name='allexpense'),
    path('allincome/', views.allincome, name='allincome'),
    path('edit-income/<int:id>/', views.edit_income, name='edit-income'),
    path('delete-income/<int:id>/', views.delete_income, name='delete-income'),
    path('edit-expense/<int:id>/', views.edit_expense, name='edit-expense'),
    path('delete-expense/<int:id>/', views.delete_expense, name='delete-expense')
]