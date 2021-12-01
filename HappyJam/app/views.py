"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

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


