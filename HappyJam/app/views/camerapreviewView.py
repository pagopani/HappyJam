from django.shortcuts import render
from django.http import HttpRequest


class camerapreviewView(object):
    """description of class"""
def CameraPreview(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CameraPreview.html',
        {
            'title':'CameraPreview',
        }
    )


