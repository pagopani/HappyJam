from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
import cv2
class previewView(TemplateView):


    template_name = 'app/Preview.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Preview'
        return context

    def post(self, request, *args, **kwargs):
        print('POST')
        cap_file = cv2.VideoCapture('app/static/app/result/result.mp4')
        cap_file.isOpened()
        cap_file.read()
        return render(request,'app/Preview.html')

   

Preview =previewView.as_view()
