from django import forms

class DisplayForm(forms.Form):
    num_rows = forms.IntegerField(label='Number of Rows', min_value=1)
    num_cols = forms.IntegerField(label='Number of Columns', min_value=1)
class CsvForm(forms.Form):
    csv_file = forms.FileField()
    num_rows = forms.IntegerField(min_value=1, max_value=100)

class UploadFileForm(forms.Form):
    file = forms.FileField()
class CsvForm(forms.Form):
    csv_url = forms.CharField(label='CSV URL')