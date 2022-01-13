"""
Definition of urls for HappyJam.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.homeView.as_view(), name='home'),
    path('instrument/', views.instrumentView.as_view(), name='Instrument'),
    path('genre/', views.genreView.as_view(), name='Genre'),
    path('video/', views.videoView.as_view(), name='Video'),
    path('camerapreview/', views.camerapreviewView.as_view(), name='CameraPreview'),
    path('continue_view/', views.continueView.as_view(), name='Continue'),
    path('preview/', views.previewView.as_view(), name='Preview'),

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
    path('edit/', views.editView.as_view(), name='edit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)