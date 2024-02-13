from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .models import Car


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'cars'
    model = Car


# For simple login page you can use LoginView but if you have complex login view you cant use this class
class LoginView(auth_views.LoginView):
    template_name = 'home/login.html'
    next_page = reverse_lazy('home:home')
