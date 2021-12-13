from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
class videoView(TemplateView):


    template_name = 'app/Video.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Video'
        return context

    def post(self, request, *args, **kwargs):
        print('POST')
        return render(request,'app/Video.html')

Video =videoView.as_view()