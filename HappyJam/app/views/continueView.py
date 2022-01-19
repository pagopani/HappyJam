from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import Movie, Single, Instrument,Music
from django.core.files.storage import FileSystemStorage
import ffmpeg
import cv2


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
                    movie = request.FILES['movie_record']
                    fileobject = FileSystemStorage()
                    u_id = request.session['uid']
                    genre = request.session['genre']
                    inst = request.session['inst']
                    filename = str(u_id) + "/" + genre + "/" +inst #ファイル名をmedia/uid/genre/inst.mp4にする
                    fileobject.save((filename+".mp4"),movie) #保存

                    #Movieテーブルに登録
                    m_data= Movie(movie_path=(filename+".mp4")) #movie_pathにuid/genre/inst.mp4を保存 
                    m_data.save()

                    #音楽抽出
                    stream = ffmpeg.input("./media/"+filename+".mp4") 
                    stream = ffmpeg.output(stream, ("./media/"+filename+".wav")) 
                    ffmpeg.run(stream)

                    #Musicテーブルに登録&Movieテーブルを更新
                    music = Music(music = (filename + ".wav"))
                    music.save()
                    m_data.music_id = music
                    m_data.save()

                    #Singleテーブルを更新
                    instrument = Instrument.objects.get(instrument_name=inst)
                    s_data = Single.objects.select_related('instrument_id').get(uid=u_id,instrument_id=instrument)
                    s_data.movie_id = m_data
                    s_data.save()
                    return HttpResponse("ajax is done")

            return render(request,'app/Continue.html')

Continue = continueView.as_view()