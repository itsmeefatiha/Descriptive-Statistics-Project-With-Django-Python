from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings 
from django.core.mail import EmailMessage
def comment_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        comment = request.POST['comment']

        email_body = {
                    
        }

        email_subject = 'comment'

        email = EmailMessage(
                    email_subject,
                    'New contact submission',
                     f'Email: {email}\nComment: {comment}',
                    'noreply@semycolon.com',
                    ['fatihabouzar450@gmail.com'],
                )
                
        email.send(fail_silently=False)

        return HttpResponse('Comment submitted successfully!')
    else:
        return render(request, 'index.html')
        
def index(request):
    return render(request,'base.html')
def navbar(request):
    return render(request,'test.html')
def home(request):
    return render(request,'index.html')
def aide(request):
    return render(request,'aide.html')
def cercle(request):
    return render(request,'cercle.html')
def histogramm(request):
    return render(request,'histogramm.html')
def ring(request):
    return render(request,'ring.html')
def horizontal(request):
    return render(request,'horizontal.html')
def radar(request):
    return render(request,'radar.html')
def area(request):
    return render(request,'area.html')
def line(request):
    return render(request,'line.html')

from django.shortcuts import render
import csv
import pandas as pd
import json,openpyxl



def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
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
        else:
            return render(request, 'import_data.html', {'error': 'File not supported.'})

        # convert dataframe to list of lists
        data = df.values.tolist()
        # get header columns
        header = list(df.columns)

        # check if form was submitted with column selections
        if request.method == 'POST' and 'columns' in request.POST:
            # get selected columns from form submission
            selected_columns = request.POST.getlist('columns')
            # convert selected columns to a list of column indices
            column_indices = [header.index(col) for col in selected_columns]

            # calculate average for each selected column
            averages = []
            for idx in column_indices:
                col_data = df.iloc[:, idx]
                col_avg = col_data.mean()
                averages.append(col_avg)

            return render(request, 'display_data.html', {'data': data, 'header': header, 'averages': averages})
        
        # if no columns were selected, show column selection form
        return render(request, 'select_columns.html', {'header': header})
        
    else:
        return render(request, 'upload_csv.html')
import pandas as pd
import urllib.request
from django.shortcuts import render

def upload_csv(request):
    if request.method == 'POST':
        url = request.POST['csv_url']
        # Télécharger le fichier CSV
        response = urllib.request.urlopen(url)
        # Charger les données CSV en utilisant csv
        reader = csv.reader(response.read().decode('utf-8').splitlines())
        data = list(reader)
        html_table = '<table>'
        for row in data:
            html_table += '<tr>'
            for col in row:
                html_table += f'<td>{col}</td>'
            html_table += '</tr>'
        html_table += '</table>'
        return render(request, 'upload_csv.html', {'html_table': html_table})
    else:
        return render(request, 'upload_csv.html')
       


# views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactUs

def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        contactUs = ContactUs(name=name, email=email, comment=comment)
        contactUs.save()
        

       

    return render(request, 'index.html')
import csv
import urllib.request
from django.shortcuts import render
from django.http import JsonResponse

import json
import pandas as pd

from django.shortcuts import render
from django.http import JsonResponse

from .forms import UploadFileForm


import pandas as pd
import json
from django.shortcuts import render
from django.http import JsonResponse

def visualize_column(request):
    if request.method == 'POST':
        # Load CSV file into pandas dataframe
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)

        # Get selected column and perform calculation if requested
        selected_column = request.POST.get('selected_column')
        selected_calculation = request.POST.get('selected_calculation')
        if selected_column:
            if selected_calculation == 'mean':
                data = df.groupby(selected_column).mean().reset_index()
            else:
                data = df[selected_column].value_counts().reset_index()
                data.columns = [selected_column, 'count']
        else:
            data = None

        # Prepare chart data
        chart_data = None
        if data is not None:
            chart_data = {
                'labels': data[selected_column].tolist(),
                'label': selected_column,
                'data': data['count'].tolist(),
            }
            chart_data = json.dumps(chart_data)

        # Render template with chart data
        return render(request, 'visualize_column.html', {'chart_data': chart_data})
    else:
        return render(request, 'visualize_column.html')

def csvvisualize(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        column_name = request.POST.get('column_name')
        df = pd.read_csv(file)
        chart_data = df[column_name].value_counts().reset_index().rename(columns={'index': column_name, column_name: 'count'})
        chart_labels = chart_data[column_name].tolist()
        chart_values = chart_data['count'].tolist()
        chart_data = {'labels': chart_labels, 'values': chart_values}
        chart_data_json = json.dumps(chart_data)
        return render(request, 'chart.html', {'chart_data': chart_data_json})
    return render(request, 'import_data.html')



