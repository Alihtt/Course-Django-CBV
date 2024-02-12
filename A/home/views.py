from django.views.generic.list import ListView
from .models import Car


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'cars'

    # For all objects
    # model = Car

    # For simple filters
    # queryset = Car.objects.filter(year__gte=2010)

    # For complex filters
    def get_queryset(self):
        return Car.objects.filter(year__gte=2010)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'Ali'
        return context
