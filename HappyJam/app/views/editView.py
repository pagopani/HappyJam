"""
Definition of views.
"""
import sys
import os
import cv2
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from moviepy.editor import VideoFileClip
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..models import Single, Movie, Music, Instrument
import mediapipe as mp
import numpy as np
import time
import moviepy.editor as me
import ffmpeg
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

class  editView(TemplateView):

    template_name = 'app/Preview.html'
    # 2つの画像を横に連結する関数
    """
    def image_hcombine(im_info1, im_info2):
        img1 = im_info1[0]                       # 1つ目の画像
        img2 = im_info2[0]                       # 2つ目の画像
    
        img = cv2.hconcat([img1, img2])          # 2つの画像を横方向に連結
        return img
    # 動画を空間方向に連結させる関数
    def m_space_hcombine(movie1, movie2, path_out, scale_factor):
        path1 = movie1[0]                                       # 1つ目の動画のパス
        path2 = movie2[0]                                       # 2つ目の動画のパス
  
        color_flag1 = movie1[1]                                 # 1つ目の動画がカラーかどうか
        color_flag2 = movie2[1]                                 # 2つ目の動画がカラーかどうか
 
    # 2つの動画の読み込み
        movie1_obj = cv2.VideoCapture(path1)
        movie2_obj = cv2.VideoCapture(path2)
    # ファイルからフレームを1枚ずつ取得して動画処理後に保存する
        i = 0                                                   # 第1ループ判定用指標
        while True:
            ret1, frame1 = movie1_obj.read()                    # 1つ目の動画のフレームを取得
            ret2, frame2 = movie2_obj.read()                    # 2つ目の動画のフレームを取得
        
            check = ret1 and ret2                               # 2つのフレームが共に取得できた時だけTrue（論理演算）
            if check == True:
                im_info1 = [frame1, color_flag1]                # 画像連結関数への引数1
                im_info2 = [frame2, color_flag2]                # 画像連結関数への引数2
                frame_mix = image_hcombine(im_info1, im_info2)  # 画像連結関数の実行

                if i == 0:
                    # 動画ファイル保存用の設定
                    fps = int(movie1_obj.get(cv2.CAP_PROP_FPS))                 # 元動画のFPSを取得
                    fps_new = int(fps * scale_factor)

                    frame_size = frame_mix.shape[:3]                            # 結合したフレームのサイズを得る
                    h = frame_size[0]                                           # フレームの高さサイズを取得
                    w = frame_size[1]                                           # フレームの横サイズを取得
                    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')         # 動画保存時のfourcc設定（mp4用）
                    video = cv2.VideoWriter(path_out, fourcc, fps_new, (w, h))  # 保存動画の仕様
                    i = i + 1                                                   # 初期ループ判定用指標を増分
                else:
                    pass
                video.write(frame_mix)                                          # 動画を保存する
            else:
                break

    # 動画オブジェクトの解放
        movie1_obj.release()
        movie2_obj.release()
        return

# ここからメイン実行文
    movie1 = ['app/static/app/movie/demo1.mp4', True]     # 元動画のパス1, カラーはTrue
    movie2 = ['app/static/app/movie/demo2.mp4', True]    # 元動画のパス2, 白黒はFalse
    path_out = 'app/static/app/movie/movie_out.mp4'        # 保存する動画のパス
    scale_factor = 1                  # FPSにかけるスケールファクター

# 複数動画を連結させる関数を実行
        m_space_hcombine(movie1, movie2, path_out, scale_factor)
    """


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Preview'
        return context

    def post(self, request, *args, **kwargs):
        #動画データの取得
        mode = request.session['mode']#モードを取得
        if mode == "single":    #Singleモードの場合
            u_id = request.session['uid'] #uidの取得
            play_data = Single.objects.filter(uid=u_id, movie_id__isnull=False).values_list("movie_id__movie_path",flat = True)#uidに該当するSingleとMovieの内部結合テーブルからmovie_pathを取得するクエリテーブルを生成 
            movie_data = list(play_data)#movie_pathが入ったリストを生成
            play_data = Single.objects.filter(uid=u_id, movie_id__isnull=False).values_list("movie_id__music_id__music",flat = True)
            music_data = list(play_data)#music(曲のパス)が入ったリストを生成
            genre = request.session['genre']
            inst = request.session['inst']
            for i in movie_data:
        # For webcam input:
               BG_COLOR = (192, 192, 192) # gray
               cap1 = cv2.VideoCapture("./media/"+i)
# 幅と高さを取得p
               width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
               height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
               size = (width, height)
#フレームレート取得
               fps = cap1.get(cv2.CAP_PROP_FPS)
#フォーマット指定
               fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
               writer = cv2.VideoWriter("app/static/app/result/"+str(u_id)+".mp4", fmt, fps, size)
#注）グレースケールの画像を出力する場合は第5引数に0を与える
               with mp_selfie_segmentation.SelfieSegmentation( 
                 model_selection=1) as selfie_segmentation:
                bg_image = cv2.VideoCapture("./app/static/app/movie/"+genre+".mp4")
                while cap1.isOpened():
                  success, image = cap1.read()
                  ret, frame = bg_image.read()
                  frame = cv2.resize(frame, dsize=(1136, 640))
                  if not success:
                     print("Ignoring empty camera frame.")
                     break


                  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
    #image2 = cv2.imread("gyazo/sample4.jpg")
    #image2 = cap2.read()
    #image2 = cv2.resize(image2, winSize)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
                  image.flags.writeable = False
                  results = selfie_segmentation.process(image)

                  image.flags.writeable = True
                  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                  condition = np.stack(
                     (results.segmentation_mask,) * 3, axis=-1) > 0.1
	  
                  if bg_image is None:
                    bg_image = np.zeros(image.shape, dtype=np.uint8)
                    bg_image[:] = BG_COLOR
                  output_image = np.where(condition, image, frame)
                  writer.write(output_image)
  
    
# 終了時処理
               writer.release()
               cap1.release()
               #cap_file = cv2.VideoCapture("app/static/app/result/result.mp4")
               #cap_file.open()
               #cap_file.read()
               cv2.destroyAllWindows()
        #動画データの取得
        #clip = me.VideoFileClip('app/static/app/result/result.mp4')
        #clip.write_videofile('app/static/app/result/result.mp4')
       
         #動画変換
        stream = ffmpeg.input("app/static/app/result/"+str(u_id)+".mp4") 
        stream = ffmpeg.output(stream, ("app/static/app/result/"+str(u_id)+genre+".mp4"),vcodec = 'libx264') 
        ffmpeg.run(stream)
        
        SAMPLE_RANGE = 20
        clip = me.VideoFileClip("app/static/app/result/"+str(u_id)+genre+".mp4")
        clip = clip.set_audio(me.AudioFileClip("media/"+str(u_id)+"/"+genre+"/"+inst+".wav"))
        clip.write_videofile("app/static/app/result/"+str(u_id)+genre+"result.mp4")


            

        #定数の定義
        ##開始から何秒をサンプリングするか
        
        # 映像と音声を結合して保存
        


        return render(request,'app/Preview.html')

edit =editView.as_view()