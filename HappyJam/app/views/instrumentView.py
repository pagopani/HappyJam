
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
        if request.method == 'POST':
            if 'pop'in request.POST:
                request.session['genre'] = 'pop'

            if 'jazz'in request.POST:
                request.session['genre'] = 'jazz'     
                
            if 'rock'in request.POST:
                request.session['genre'] = 'rock'
        genre=request.session['genre']
        use=request.session['use'] 
        print(genre,use)
        return render(request,'app/Instrument.html')

Instrument =instrumentView.as_view()
