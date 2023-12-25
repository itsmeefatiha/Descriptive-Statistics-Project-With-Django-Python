from django.urls import path 
from .views  import upload_file, calculate,calculate_statistics, charts , my_view ,line_chart,pie_chart
from . import views

urlpatterns = [
     path('upload-file', upload_file, name='upload-file'),
     path('urlcsv',views.upload_csv,name="urlcsv"),
    # path('upload/', upload_csv, name='upload-csv'),
     path('navbar', my_view, name='navbar'), 
     path('chart', charts, name='chart'),
    # path('download_csv/', download_csv, name='download_csv'),
   
      path('calculate',calculate_statistics, name='calculate'),
      path('line_chart',line_chart, name='line_chart'),
      path('pie_chart',pie_chart, name='pie_chart'),
     path('test/',calculate, name='test'),
]
