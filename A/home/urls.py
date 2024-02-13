from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<str:name>/', views.SingleCar.as_view(), name='single_car')
]
