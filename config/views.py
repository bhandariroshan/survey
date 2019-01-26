from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/success.html'

    def get(self, request, *args, **kwargs):
        """Method to select record page."""
        context = {}

        return HttpResponseRedirect('/admin/')


class SurveyView(TemplateView):
    template_name = 'pages/survey.html'

    def get(self, request, *args, **kwargs):
        """Method to select record page."""
        context = {}

        return HttpResponseRedirect('//')
