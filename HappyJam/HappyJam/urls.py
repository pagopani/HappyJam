"""
Definition of urls for HappyJam.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('Instrument/', views.Instrument, name='Instrument'),
    path('Genre/', views.Genre, name='Genre'),
    path('Video/', views.Video, name='Video'),
    path('CameraPreview/', views.CameraPreview, name='CameraPreview'),
    path('Continue/', views.Continue, name='Continue'),
    path('Preview/', views.Preview, name='Preview'),

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
]
