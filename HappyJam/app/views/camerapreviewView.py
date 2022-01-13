from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import User,Single,Instrument
from django.db import IntegrityError



class camerapreviewView(TemplateView):
    template_name = 'app/CameraPreview.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'CameraPreview'
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            u_id = request.session['uid'] 
            user = User.objects.get(id=u_id)
            if 'guitar'in request.POST:
                inst =Instrument.objects.get(id=1)
                request.session['inst'] = 'guitar'
                try:
                    single = Single(uid =user,instrument_id=inst)
                    single.save()
                except IntegrityError as e:
                    if 'unique constraint' in e.message: # or e.args[0] from Django 1.10
                        single=Single.objects.get(uid=u_id,instrument_id=1)

            if 'bass'in request.POST:
                request.session['inst'] = 'bass'
                inst =Instrument.objects.get(id=2)
                try:
                    single = Single(uid =user,instrument_id=inst)
                    single.save()
                except IntegrityError as e:
                    if 'unique constraint' in e.message: # or e.args[0] from Django 1.10
                        single=Single.objects.get(uid=u_id,instrument_id=2)
                
            if 'drum'in request.POST:
                request.session['inst'] = 'drum'
                inst =Instrument.objects.get(id=3)
                try:
                    single = Single(uid =user,instrument_id=inst)
                    single.save()
                except IntegrityError as e:
                    if 'unique constraint' in e.message: # or e.args[0] from Django 1.10
                        single=Single.objects.get(uid=u_id,instrument_id=3)
            
        inst=request.session['inst'] 
        print(inst)
        return render(request,'app/CameraPreview.html')


CameraPreview = camerapreviewView.as_view()