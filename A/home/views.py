from django.views.generic import ListView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import CarCreateForm
from .models import Car
from django.contrib import messages


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'cars'
    model = Car


class CarCreateView(FormView):
    template_name = 'home/create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        self._create_car(form.cleaned_data)
        messages.success(self.request, 'Your car created successfully', 'success')
        return super().form_valid(form)

    def _create_car(self, data):
        Car.objects.create(name=data['name'], owner=data['owner'], year=data['year'])
