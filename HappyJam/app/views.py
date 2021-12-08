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

def edit(request):
    #定数の定義
    #開始から何秒をサンプリングするか 
    SAMPLE_RANGE = 60 
    # 映像と音声を結合して保存 
    clip = mp.VideoFileClip('app/static/app/movie/demo.mp4').subclip()
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


