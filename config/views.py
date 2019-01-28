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

        survey = Survey.objects.get(survey_number=survey)
        code = Codes.objects.get(code=code)

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

        survey = kwargs.get('survey')
        survey = Survey.objects.get(survey_number=survey)

        newHtml = '<div id="surveyDiv" style=" margin-top: 100px; text-align: center;">'
        newHtml += '<label style="margin-bottom: 30px;"> <strong> How much do you agree with the statement you saw? </strong> </label>'
        newHtml += '<div class="btn-group btn-group-toggle" id="test">'

        newHtml += '<label class="btn btn-secondary"  style="margin-right: 10px;">'
        newHtml += '<input type="radio" value="Highly disagree" name="choice" autocomplete="off"> Highly disagree'
        newHtml += '</label>'

        newHtml += '<label class="btn btn-secondary" style="margin-right: 10px;">'
        newHtml += '<input type="radio" value="Disagree" name="choice" autocomplete="off"> Disagree'
        newHtml += '</label>'

        newHtml += '<label class="btn btn-secondary" style="margin-right: 10px;">'
        newHtml += '<input type="radio" value="Neutral" name="choice" autocomplete="off"> Neutral'
        newHtml += '</label>'

        newHtml += '<label class="btn btn-secondary" style="margin-right: 10px;">'
        newHtml += '<input type="radio"  value="Agree" name="choice" autocomplete="off"> Agree'
        newHtml += '</label>'

        newHtml += '<label class="btn btn-secondary" style="margin-right: 10px;">'
        newHtml += '<input value="Highly agree" type="radio" name="choice" autocomplete="off"> Highly agree'
        newHtml += '</label>'

        newHtml += '</div>'
        newHtml += '</div>'

        return JsonResponse({
            'status': 'success',
            'thanks_html': '<p style="margin-top: 50px; text-align: center;">Thanks!</p>',
            'options_html': newHtml,
            'survey_html': survey.html
        })
