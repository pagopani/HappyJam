from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class camerapreviewView(TemplateView):
    template_name = 'app/CameraPreview.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'CameraPreview'
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return render(request,'app/CameraPreview.html')


CameraPreview = camerapreviewView.as_view()