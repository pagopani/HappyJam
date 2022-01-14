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
                #Ajax 処理を別メソッドに切り離す
                if request.FILES['movie_record']:
                    movie = request.FILES['movie_record'] #formからmovie_recordをmovieに取得
                    fileobject = FileSystemStorage() #ファイルオブジェクトを呼び出し
                    uid = request.session['uid']
                    genre = request.session['genre']
                    inst = request.session['inst']
                    filename = str(uid) + "/" + genre + "/" +inst + ".mp4" #保存先＆ファイル名をmedia直下のuid/genre/inst.mp4にする
                    fileobject.save(filename,movie) #media/(uid)/(genre)/(inst).mp4にmovieを保存
                    del request.session['p_flag']
                    request.session['p_flag'] = 1 #録画完了フラグ
                    return HttpResponse("ajax is done")

            return render(request,'app/Continue.html')

Continue = continueView.as_view()