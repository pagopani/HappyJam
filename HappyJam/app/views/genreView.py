
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

    def set_cookie(self,key,value='', max_age=None, expires=None, path='/',domain=None, secure=False, httponly=False, samesite=None):
        a = b
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'single'in request.POST:
                request.session['mode'] = 'single'

            if 'multi'in request.POST:
                request.session['mode'] = 'multi'
        
        mode=request.session['mode'] 
        print(mode)
        return render(request,'app/Genre.html')

genre =genreView.as_view()