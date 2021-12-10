from django.shortcuts import render
from django.http import HttpRequest


class videoView(object):
    """description of class"""
def Video(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Video.html',
        {
            'title':'Video',
        }
    )


