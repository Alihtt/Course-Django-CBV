from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CarCreateView.as_view(), name='create'),
]
