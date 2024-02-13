from django.views.generic import ListView, MonthArchiveView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .models import Car


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'cars'
    model = Car


class MonthCar(MonthArchiveView):
    template_name = 'home/home.html'
    context_object_name = 'cars'
    model = Car
    date_field = 'created'
    month_format = "%m"
