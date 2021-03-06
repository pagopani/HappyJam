"""
Definition of views.
"""
import sys
import os
import numpy as np
import moviepy.editor as mp
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from moviepy.editor import VideoFileClip
import cv2




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def Instrument(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Instrument.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def Genre(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Genre.html',
        {
            'title':'Genre',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def Video(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Video.html',
        {
            'title':'Video',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def CameraPreview(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CameraPreview.html',
        {
            'title':'CameraPreview',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Continue(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Continue.html',
        {
            'title':'Continue',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def Preview(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Preview.html',
        {
            'title':'Preview',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
# 2つの画像を横に連結する関数
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

def edit(request):

    #定数の定義
    #開始から何秒をサンプリングするか 
    SAMPLE_RANGE = 60 
    # 映像と音声を結合して保存 
    clip = mp.VideoFileClip('app/static/app/movie/movie_out.mp4').subclip()
    clip.write_videofile('app/static/app/movie/main.mp4', audio='app/static/app/music/rock/rock.mp3')

    return render(
        request,
        'app/Preview.html',
        {
            'title':'Preview',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
)


