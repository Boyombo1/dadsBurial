from django.contrib import admin

# Register your models here.
from .models import Income, Expence

admin.site.register(Income)
admin.site.register(Expence)