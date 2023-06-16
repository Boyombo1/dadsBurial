from django.urls import path, include
from . import views

urlpatterns = [
    path('addincome/', views.income_add, name='addincome'),
    path('addexpense/', views.expence_add, name='addexpense'),
    path('allexpense/', views.allexpence, name='allexpense'),
    path('allincome/', views.allincome, name='allincome')
]