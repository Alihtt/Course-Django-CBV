from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveDestroyAPIView
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin


# class Home(RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if instance.name == 'Nisan':
#             return Response('Sorry.....')
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


class Home(RetrieveDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.name == 'Nisan':
            return Response('Sorry.....')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
