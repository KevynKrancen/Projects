
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    # path('Datareceive', views.Datareceive, name='Datareceive'),
    path('NaiveBayestests', views.NaiveBayestests, name='NaiveBayestests'),
    path('id3tests', views.id3tests, name='id3tests'),
    path('Addfile', views.Addfile, name='Addfile'),
    path('simple_upload', views.simple_upload, name='simple_upload'),
    path('NaiveNayesown', views.NaiveNayesown, name='NaiveNayesown'),
    path('MyNaiveBayesResult', views.MyNaiveBayesResult, name='MyNaiveBayesResult'),
    path('NaiveBayesSklearn', views.NaiveBayesSklearn, name='NaiveBayesSklearn'),
    path('MyID3', views.MyID3, name='MyID3'),   
    path('SklearnID3', views.SklearnID3, name='SklearnID3'), 
    path('KNNCLASS', views.KNNCLASS, name='KNNCLASS'),   
]