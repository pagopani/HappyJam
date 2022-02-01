from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import Movie, Single, Instrument,Music
from django.core.files.storage import FileSystemStorage
import ffmpeg
from mutagen.easyid3 import EasyID3
import mutagen.id3

class continueView(TemplateView):
    template_name = 'app/Continue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Continue'
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            u_id = request.session['uid']
            genre = request.session['genre']
            inst = request.session['inst']
            filename = str(u_id) + "/" + genre + "/" +inst
            
            if request.is_ajax():
                #Ajax 処理を別メソッドに切り離す
                if request.FILES['movie_record']:
                    movie = request.FILES['movie_record']
                    fileobject = FileSystemStorage()
                    fileobject.save((filename+".webm"),movie) #保存
                    """try:
                        tags = EasyID3(str("./media/"+filename+".mp4"))
                    
                    except mutagen.id3.ID3NoHeaderError:
                        tags = mutagen.File(str("./media/"+filename+".mp4"), easy=True)
                        tags.add_tags()
                    
                    tag["length"]=81000
                    tags.save()"""
                    return HttpResponse("ajax is done")

            #動画変換
            stream = ffmpeg.input(("./media/"+filename+".webm")) 
            stream = ffmpeg.overwrite_output(stream, ("./media/"+filename+".mp4")) 
            ffmpeg.run(stream)
            
            #音楽抽出
            stream = ffmpeg.input("./media/"+filename+".mp4") 
            stream = ffmpeg.overwrite_output(stream, ("./media/"+filename+".wav")) 
            ffmpeg.run(stream)

            #Musicテーブルに登録&Movieテーブルも登録
            music = Music(music = (filename + ".wav"))
            music.save()
            m_data = Movie(movie_path=(filename + ".mp4"),music_id=music)
            m_data.save()

            #Singleテーブルを更新
            instrument = Instrument.objects.get(instrument_name=inst)
            s_data = Single.objects.select_related('instrument_id').get(uid=u_id,instrument_id=instrument)
            s_data.movie_id = m_data
            s_data.save()

            request.session['p_flag'] = 1
            
            return render(request,'app/Continue.html')

Continue = continueView.as_view()