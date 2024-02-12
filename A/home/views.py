from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Car


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'cars'
    model = Car


class CarDeleteView(DeleteView):
    template_name = 'home/delete.html'
    model = Car
    success_url = reverse_lazy('home:home')


class CarUpdateView(UpdateView):
    template_name = 'home/update.html'
    model = Car
    fields = ('name', 'year')
    success_url = reverse_lazy('home:home')
