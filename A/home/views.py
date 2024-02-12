from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Car


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'cars'
    model = Car


class CarDetailView(DetailView):
    template_name = 'home/detail.html'
    model = Car
    slug_field = 'name'
    slug_url_kwarg = 'car_name'
