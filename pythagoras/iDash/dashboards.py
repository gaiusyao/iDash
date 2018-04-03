import datetime

from django.db.models import Count
from django.utils import timezone
from django.utils.timesince import timesince
from controlcenter import Dashboard, widgets, app_settings
from .models import Order, Pizza, Restaurant

class MenuWidget(widgets.ItemList):
    # This widget displays a list of pizzas ordered today
    # in the restaurant
    title = 'Ciao today orders'
    model = Pizza
    list_display = ['name', 'ocount']

class MyDashboard(Dashboard):
    widgets = (
        MenuWidget,
    )