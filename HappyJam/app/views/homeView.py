from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name = 'app/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'home'
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            return render(request,'app/index.html')


index = homeView.as_view()