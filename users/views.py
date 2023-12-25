import pandas as pd
from django.shortcuts import render
from .forms import  UploadFileForm , CsvForm 
import matplotlib 
from django.contrib import messages
import numpy as np
import json



   

def my_view(request):
    return render(request , 'users/index3.html')







from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import lxml
def upload_file(request):
    
    if request.method == 'POST':

            
            file = request.FILES['file']
            file_extension = file.name.split('.')[-1]
        
            if file_extension == 'csv':
            # read csv data as pandas dataframe
               df = pd.read_csv(file)
            elif file_extension == 'json':
            # read json data as pandas dataframe
               df = pd.read_json(file)
            elif file_extension in ['xls', 'xlsx']:
            # read excel data as pandas dataframe
               df = pd.read_excel(file)
            elif file_extension == 'xml':
                    df = pd.read_xml(file)

            else:
                    raise ValidationError('Unknown file type')
                
            num_rows = request.POST.get('num_rows', None)
            num_cols = request.POST.get('num_cols', None)
            request.session['df'] = df.to_dict()

            if num_rows:
                df = df.head(int(num_rows))

            if num_cols:
                df = df.iloc[:, :int(num_cols)]

            context = {
                    'dataframe': df.to_html(classes='table table-striped'),
                    'df': df,
                }
            return render(request, 'users/csv_display.html', context)
            
   
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'users/import.html', context)

    
def calculate_statistics(request):

    if request.method == 'POST'   :
        df_dict = request.session.get('df')
        df = pd.DataFrame(df_dict)
        selected_calculation = request.POST['selected_calculation']
        column_name = request.POST['column_name']
       
       
        selected_column = df.loc[:, column_name]
        
        if selected_column.dtype == 'int64' or selected_column.dtype == 'float64' :
       
          if selected_calculation == 'mean':
             result =  selected_column.mean()
          elif selected_calculation == 'median':
             result = selected_column.median()
          elif selected_calculation == 'mode':
             result = selected_column.mode()[0]
          elif selected_calculation == 'min':
             result  = selected_column.min()
          elif selected_calculation == 'max':
             result =  selected_column.max() 
          elif selected_calculation == 'range':
             min_value = selected_column.min()
             max_value =  selected_column.max() 
             result = max_value - min_value
          elif selected_calculation == 'lécart_type':
             result = selected_column.std()
          elif selected_calculation == 'variance':
             result = selected_column.var()
          elif selected_calculation == 'somme':
             result = selected_column.sum()
          elif selected_calculation == 'quartiles':
             q1 = selected_column.quantile(0.25)
             q3 = selected_column.quantile(0.75)
             result = q3 - q1
         
          context = {
            'selected_column': column_name ,
            'selected_calculation': selected_calculation.capitalize(),
            'result': result
            }

        else:
                # Render an error message if the selected column contains non-numeric values
            context = {
                 'error_message': f'The selected column "{column_name}" contains non-numeric values.',
                }
        return render(request, 'users/test_calcule.html', context)
    else:
        context = {
                 'error_message': f'not data found',
                }
        return render(request, 'users/test_calcule.html')
     

def calculate(request):

    if request.method == 'POST' :
        df_dict = request.session.get('df')
        df = pd.DataFrame(df_dict)
        selected_calculation = request.POST['selected_calculation']
       
        column_x = request.POST['column_x']
        column_y = request.POST['column_y']
        selected_columns = df[[column_x, column_y]]
       
       
        selected_columns = selected_columns.apply(pd.to_numeric, errors='coerce')
        selected_columns = selected_columns.dropna()
        if all(selected_columns.dtypes == 'float64') or all(selected_columns.dtypes == 'int64')  :
          
           if selected_calculation == 'covariance':
             result = selected_columns.cov().iloc[0, 1]
           else:
             result = selected_columns.corr().iloc[0, 1]
          
           context = {
            'column_x':column_x,
            'column_y':column_y,
            'selected_calculation': selected_calculation.capitalize(),
            'result': result
            }

        else:
                # Render an error message if the selected column contains non-numeric values
            context = {
                 'error_message': f'The selected column "{column_x}" contains non-numeric values.',
                }
        return render(request, 'users/suite_calcule.html', context)
    else:
        return render(request, 'users/suite_calcule.html')
     









import urllib.request
import csv

def upload_csv(request):
    if request.method == 'POST':
        url = request.POST['csv_url']
        # Télécharger le fichier CSV
        response = urllib.request.urlopen(url)
        # Charger les données CSV en utilisant csv
        reader = csv.reader(response.read().decode('utf-8').splitlines())
        data = list(reader)
        html_table = '<table table-striped>'
        for row in data:
            html_table += '<tr>'
            for col in row:
                html_table += f'<td>{col}</td>'
            html_table += '</tr>'
        html_table += '</table>'
        return render(request, 'users/csv_display.html', {'html_table': html_table})
    else:
        return render(request, 'users/url_upload.html')
           
           


















import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chartjs.views.lines import BaseLineChartView

class BarChartJSONView(BaseLineChartView):

    def get_labels(self):
        """Return labels for the chart"""
        return self.data['labels']

    def get_providers(self):
        """Return names of datasets"""
        return ['Data']

    def get_data(self):
        """Return datasets to plot"""
        return [self.data['values']]

@csrf_exempt
def chart(request):
    if request.method == 'POST':
        df_dict = request.session.get('df')
        df = pd.DataFrame(df_dict)
    
        column_name = request.POST['column_name']
        data = df[column_name].astype(float) # example: convert to float
        chart_data = {'labels': list(df.index), 'data': list(data)}
        return render(request, 'users/test_visualization.html', {'chart_data': chart_data})
    return render(request, 'users/calculate_average.html')

import pandas as pd
from django.shortcuts import render



def calculate_statistic(request):
    if request.method == 'POST':
        
        selected_column = request.POST['selected_column']
        selected_calculation = request.POST['selected_calculation']
        csv_file = request.FILES['file']
        col = df.columns.to_numpy
        df = pd.read_csv(csv_file)
        column = df[selected_column]
        if selected_calculation == 'mean':
            result = round(column.mean(), 2)
        elif selected_calculation == 'median':
            result = round(column.median(), 2)
        elif selected_calculation == 'mode':
            result = column.mode().tolist()
        elif selected_calculation == 'min':
            result = column.min()
        elif selected_calculation == 'max':
            result = column.max()
        context = {
            'selected_column': selected_column,
            'selected_calculation': selected_calculation.capitalize(),
            'result': result,
            'col':  col 
        }
        return render(request, 'users/test_calcule.html', context)
    return render(request, 'users/test_calcule.html')


    
import matplotlib.pyplot as plt 
import io
import base64
def line_chart(request):
    if request.method == 'POST':
        # Parse uploaded CSV file
        df_dict = request.session.get('df')
        df = pd.DataFrame(df_dict)
        # Extract selected column
        column_name = request.POST['column_name']
        selected_column = df[column_name]

        # Generate chart
        plt.plot(selected_column)
        plt.xlabel('X Label')
        plt.ylabel('Y Label')
        plt.title('Title')
        plt.grid(True)

        # Convert chart to base64 encoded string
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')

        # Pass chart data to HTML template and render response
        context = {'graph': graph}
        return render(request, 'users/line_chart.html', context)

    else:
        return render(request, 'users/simple_chart.html')
def pie_chart(request):
    if request.method == 'POST':
        # Parse uploaded CSV file
        df_dict = request.session.get('df')
        df = pd.DataFrame(df_dict)
        # Extract selected column
        column_name = request.POST['column_name']
        selected_column = df[column_name]

        # Generate chart
        plt.pie(selected_column)
        plt.xlabel( column_name)
        plt.ylabel('Y Label')
        plt.title('Title')
        plt.grid(True)

        # Convert chart to base64 encoded string
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graph = base64.b64encode(image_png)
        pie = graph.decode('utf-8')

        # Pass chart data to HTML template and render response
        context = {'pie': pie}
        return render(request, 'users/pie_chart.html', context)

    else:
        return render(request, 'users/simple_chart.html')
    
 
 
import chartjs

def visualize_statisti(request):
   if request.method == 'POST':
      df_dict = request.session.get('df')
      df = pd.DataFrame(df_dict)
     # extract the columns of interest
      colonne1 = request.POST['column_1']
      colonne2= request.POST['column_2']
      data = df[[colonne1, colonne2]]

      chart = chartjs.Chart("mon_graphique", {
        "type": "bar",
        "data": {
            "labels": data[colonne1].tolist(),
            "datasets": [{
                "label": colonne1,
                "data": data[colonne1].tolist(),
                "backgroundColor": "#F9A825"
            },
            {
                "label": colonne2,
                "data": data[colonne2].tolist(),
                "backgroundColor": "#7CB342"
            }]
        },
        "options": {
            "title": {
                "display": True,
                "text": "Graphique à barres avec deux colonnes choisies par l'utilisateur"
            }
           }
           })

      chart_html = chart.render()
      return render('users/visualization.html', chart=chart_html)
   
   else:
       return render(request, 'users/calculate_average.html')
    # Renvoi de la page avec le graphique
   

def charts(request):
    return render(request , 'users/visualization.html')
    