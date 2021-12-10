from django.shortcuts import render
from django.http import HttpRequest

class previewView(object):
    """description of class"""
def Preview(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Preview.html',
        {
            'title':'Preview',
        }
    )


