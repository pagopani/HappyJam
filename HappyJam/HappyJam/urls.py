"""
Definition of urls for HappyJam.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.homeView.as_view(), name='home'),
    path('instrument/', views.instrumentView.as_view(), name='Instrument'),
    path('genre/', views.genreView.as_view(), name='Genre'),
    path('video/', views.videoView, name='Video'),
    path('camerapreview/', views.camerapreviewView, name='CameraPreview'),
    path('continue_view/', views.continueView, name='Continue'),
    path('preview/', views.previewView, name='Preview'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('edit/', views.editView, name='edit'),
]
