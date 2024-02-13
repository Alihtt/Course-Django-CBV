from .models import Car
from .serializers import CarSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class Home(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class SingleCar(RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = 'name'
