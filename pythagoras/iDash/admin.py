from django.contrib import admin
from .models import Order, Pizza, Restaurant

admin.site.register(Order)
admin.site.register(Pizza)
admin.site.register(Restaurant)