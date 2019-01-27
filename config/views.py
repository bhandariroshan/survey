from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from surveyapp.models import Survey, Codes
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render


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

        survey = kwargs.get('survey')
        code = kwargs.get('code')

        print("Survey::", survey, " Code:: ", code)
        survey = Survey.objects.get(survey_number=survey)
        code = Codes.objects.get(code=code)

        code.is_used = True
        code.save()

        context['survey'] = survey
        context["code"] = code

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """Method to select record page."""

        context = {}
        code = kwargs.get('code')
        code = Codes.objects.get(code=code)

        code.is_used = True
        code.answer = request.POST.get('value')
        code.save()

        print(code,request.POST.get('value'))
        return JsonResponse({'status': 'success'})
