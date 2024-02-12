from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('delete/<int:pk>/', views.CarDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.CarUpdateView.as_view(), name='update'),
]
