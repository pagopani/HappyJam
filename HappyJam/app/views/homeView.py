from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name = 'app/index.html'

    def dispatch(self, request, *args, **kwargs):
        print('DISPATCH')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'home'
        return context

    def get(self, request, *args, **kwargs):
        print('GET')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('POST')
        return render(request,'app/Genre.html',context)

index = homeView.as_view()