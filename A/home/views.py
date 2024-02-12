from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    http_method_names = ['get', 'options']

    def get(self, request):
        return render(request, 'home/home.html')

    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['user'] = request.user
        response.headers['host'] = 'localhost'
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, 'method_not_allowed.html')
