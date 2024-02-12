from django.views.generic import TemplateView, RedirectView
from .models import Car


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class Two(RedirectView):
    pattern_name = 'home:home'

    def get_redirect_url(self, *args, **kwargs):
        print('=' * 90)
        print('Processing your request')
        print('Redirecting...')
        return super().get_redirect_url(*args, **kwargs)
