from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:car_name>/', views.CarDetailView.as_view(), name='car_detail'),
]
