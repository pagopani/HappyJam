from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
class previewView(TemplateView):


    template_name = 'app/Preview.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Preview'
        return context

    def post(self, request, *args, **kwargs):
        print('POST')
        return render(request,'app/Preview.html')

Preview =previewView.as_view()
