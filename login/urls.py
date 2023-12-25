from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.home,name="home"),
    path('upload_file/',views.upload_file,name="upload"),
    path('',views.comment_form,name="contact"),
    path('aide/',views.aide,name="aide"),
    path('urlcsv/',views.upload_csv,name="urlcsv"),
    path('contactUs',views.contactUs, name='contactUs'),
    path('histogramm/',views.histogramm, name='histogramm'),
    path('cercle/',views.cercle, name='cercle'),
    path('ring/',views.ring, name='ring'),
    path('area/',views.area, name='area'),
    path('line/',views.line, name='line'),
    path('horizontal/',views.horizontal, name='horizontal'),
    path('radar/',views.radar, name='radar'),
    path('visualize_column/',views.visualize_column,name='visualize_column'),
    path('csvvisualize/',views.csvvisualize,name='csvvisualize'),
]