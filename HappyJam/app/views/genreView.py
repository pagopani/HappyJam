
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView


class genreView(TemplateView):
    template_name = 'app/genre.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'genre'
        return context

    def post(self, request, *args, **kwargs):
        print('POST')
        return render(request,'app/Genre.html')

genre =genreView.as_view()

