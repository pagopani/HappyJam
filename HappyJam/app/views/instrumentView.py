
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import User,Single


class instrumentView(TemplateView):
    template_name = 'app/instrument.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'instrument'
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            mode=request.session['mode'] 
            if mode == "single":
                user = User(created_date ="")
                user.save()
                request.session['uid'] = user.id
                u_id=request.session['uid']
                print(u_id)

            if 'pop'in request.POST:
                request.session['genre'] = 'pop'

            if 'jazz'in request.POST:
                request.session['genre'] = 'jazz'     
                
            if 'rock'in request.POST:
                request.session['genre'] = 'rock'
        genre=request.session['genre']
        
        print(genre,mode)
        #録画完了したことあるかのフラグ
        if "p_flag" in request.session:
            print(request.session['p_flag'])
        else:
            request.session['p_flag'] = 0
        
    
        return render(request,'app/Instrument.html')

Instrument =instrumentView.as_view()
