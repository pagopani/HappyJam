
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class instrumentView(TemplateView):
    template_name = 'app/instrument.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'instrument'
        return context

    def post(self, request, *args, **kwargs):
        print('POST')
        return render(request,'app/Instrument.html')

Instrument =instrumentView.as_view()
