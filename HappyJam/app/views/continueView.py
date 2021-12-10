from django.shortcuts import render
from django.http import HttpRequest


class continueView(object):
    """description of class"""
    def Continue(request):
        assert isinstance(request, HttpRequest)
        return render(
        request,
        'app/Continue.html',
        {
            'title':'Continue',
        }
    )