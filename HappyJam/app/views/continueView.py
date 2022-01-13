from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import Movie
from django.core.files.storage import FileSystemStorage


class continueView(TemplateView):
    template_name = 'app/Continue.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Continue'
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.is_ajax():
                """Ajax 処理を別メソッドに切り離す"""
                if request.FILES['movie_record']:
                    movie = request.FILES['movie_record']
                    fileobject = FileSystemStorage()
                    uid = request.session['uid']
                    genre = request.session['genre']
                    inst = request.session['inst']
                    filename = str(uid) + "/" + genre + "/" +inst + ".mp4"
                    fileobject.save(filename,movie)
                    
                    return

            return render(request,'app/Continue.html')

Continue = continueView.as_view()